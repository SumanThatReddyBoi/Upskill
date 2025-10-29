from rich import Panel
from rich.console import Console
from rich.text import Text
from rich.table import Table
from wordfreq import zipf_frequency, top_n_list
import random

console = Console()
console.print(Panel("Welcome to Wordle!", title="Wordle", style="bold cyan"))

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
    t=Text()
    for ch, s, in zip(guess.upper(), status):
        if s == "green": 
            color = "green"
            fg = "black" 
        elif s == "yellow":
            color = "yellow"
            fg = "black" 
        else:
            color = "grey23"
            fg = "white"
        t.append(f" {ch} ", style=f"bold {fg} on {color}")
        t.append(" ")
    console.print(t)

def is_a_real_word(word: str) -> bool:
    return zipf_frequency(word, 'en') > 0

def main():
    secret = get_random_word()
    MAX_GUESSES = 6

    used_guesses = set()

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

        if all(s == "green" for s in status):
            console.print("[green]Congratulations! You have guessed the word![/]")
            break

    else:
        console.print(f"[bold red]Out of guesses! The word was {secret.upper()}[/]")

if __name__ == "__main__":
    main()



