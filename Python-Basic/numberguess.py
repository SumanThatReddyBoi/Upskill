import random
import sys

print("Welcome to the Number Guessing Game!")

print("The number is between 1-1000")
print("Let's get started!")

generated = random.randint(1, 1000)
while(1):
    while(1):
        user = int(input("Enter your guess: "))
        if user==generated:
            print("Bingo! You got it!")
            break
        elif user<generated:
            print("That's a bit low! Try Again.")
        elif user>generated:
            print("That's a bit high. Try Again!")


    while(1):
        again=input("Do you want to play again? (Y/N)")
        if again=='Y':
            break
        elif again=='N':
            sys.exit(0)
        else:
            print("Invalid Responce")

