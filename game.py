# game.py
import random


print("Rock, Paper, Scissors, Shoot!")
user_choice=input("choose 'paper' or 'rock' or 'scissors'")
print("User chose:")
print (user_choice)

options=["rock","paper","scissors"]
computer_choice=random.choice(options)
print("Computer chose:")
print(computer_choice)

