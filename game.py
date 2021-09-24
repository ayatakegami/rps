# game.py
import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print("Hi", x)

import random
print("Welcome to my rock paper scissors game!")
print("------------------------------")
print("Rock, Paper, Scissors, Shoot!")
user_choice=input("choose 'paper' or 'rock' or 'scissors'")
if user_choice not in ['rock', 'paper', 'scissors']:
    print("invalid user choice, try again")
    exit ()

print("User chose:")
print (user_choice)

options=["rock","paper","scissors"]
computer_choice=random.choice(options)
print("Computer chose:")
print(computer_choice)

if computer_choice == "rock" and user_choice=="scissors":
    print("Computer wins!!")
elif computer_choice == "rock" and user_choice=="paper":
    print("User wins!!")


elif computer_choice=="paper" and user_choice=="scissors":
    print("User wins!!")
elif computer_choice=="paper" and user_choice=="rock":
    print("Computer wins!!")


elif computer_choice == "scissors" and user_choice=="rock":
    print("User wins!!")
elif computer_choice == "scissors" and user_choice=="paper":
    print("Computer wins!!")

if computer_choice == user_choice:
    print("It's a tie, try again!")
print("------------------------------")
print ("Thanks for playing!")