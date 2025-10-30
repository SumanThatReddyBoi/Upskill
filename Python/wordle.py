from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.console import Group
from wordfreq import zipf_frequency, top_n_list
import random
import string

console = Console()
letter_status = {ch: "white" for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

def get_random_word() -> str:
    words = [w.lower() for w in top_n_list("en", 10000) if len(w) == 5]
    return random.choice(words)

def gradeGuess(word, guess):
    result=[]
    for i in range(len(word)):
        if guess[i] == word[i]:
            result.append("green")
        elif guess[i] in word:    
            result.append("yellow")
        else:
            result.append("gray")
    return result


def renderGuess(guess, status, console):
    global letter_status
    t = Text()
    for ch, s in zip(guess.upper(), status):
        if s == "green":
            color, fg = "green", "black"
        elif s == "yellow":
            color, fg = "yellow", "black"
        else:
            color, fg = "grey23", "white"

        prev = letter_status[ch]
        if prev == "white" or (prev == "grey23" and color != "white") or (prev == "yellow" and color == "green"):
            letter_status[ch] = color

        t.append(f" {ch} ", style=f"bold {fg} on {color}")
        t.append(" ")

    console.print(t)


def is_a_real_word(word: str) -> bool:
    return zipf_frequency(word, 'en') > 0

def render_alphabet(status_dict):
    t = Text()
    for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1):
        color = letter_status.get(ch, "white")

        if color == "green":
            style = "bold black on green"
        elif color == "yellow":
            style = "bold black on yellow"
        elif color == "grey23":
            style = "bold white on grey23"
        else:
            style = "dim white"
        t.append(f" {ch} ", style=style)
        t.append("  ")
        if i % 9 == 0:
            t.append("\n\n")
    alphabet_section = Align.center(t)
    title_text = Align.center(Text("🎯  W O R D L E  🎯", style="bold cyan underline"),)
    separator = Align.center(Text("─" * 35, style="dim cyan"))
    content = Group(title_text, separator, alphabet_section)
    panel = Panel(content, border_style="bright_cyan", expand=False, padding=(1, 4), title="[bold cyan]Wordle Tracker[/bold cyan]")
    console.print(panel)

def main():
    secret = get_random_word()
    MAX_GUESSES = 6

    used_guesses = set()

    render_alphabet(letter_status)

    for attempt in range(1, MAX_GUESSES+1):
        while True:
            guess=input(f"Guess {attempt}/{MAX_GUESSES}: ").lower().strip()

            if len(guess) != len(secret):
                console.print("[red]Please enter a five-letter word![/]")
                continue

            if not guess.isalpha():
                console.print("[red]Enter letters only please![/]")
                continue

            if not is_a_real_word(guess):
                console.print("[red]Enter valid English Words Only![/]")
                continue    

            if guess in used_guesses:
                console.print("[red]Make a new guess, this word has already been guessed![/]")
                continue

            used_guesses.add(guess)
            break

        status = gradeGuess(secret, guess)
        renderGuess(guess, status, console)

        render_alphabet(letter_status)

        if all(s == "green" for s in status):
            console.print("[green]Congratulations! You have guessed the word![/]")
            break

    else:
        console.print(f"[bold red]Out of guesses! The word was {secret.upper()}[/]")

if __name__ == "__main__":
    main()



