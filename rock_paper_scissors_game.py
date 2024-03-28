# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

choices = ("rock", "paper", "scissors")
run = True

while run:

    user = None
    computer = random.choice(choices)

    while user not in choices:
        user = input("Enter a choice (rock, paper, scissors): ")

    print(f"user: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        run = False

print("Thanks for playing!")