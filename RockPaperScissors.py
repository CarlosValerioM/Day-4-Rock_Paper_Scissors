#!/usr/bin/env python3
"""
RockPaperScissors.py - A simple Rock, Paper, Scissors game.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/08
License: MIT
Dependencies: None (built-in functions only)

Description:
This script implements the classic Rock, Paper, Scissors game.
The user plays against the computer, which randomly selects an option.

The game follows these rules:
- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.
- If both choices are the same, it's a tie.

Usage:
Run the script and follow the prompts:
    python RockPaperScissors.py

Example Output:
    Choose Rock, Paper, or Scissors: Rock
    Computer chose Scissors
    You win!
"""
# Importing the random module to generate random numbers
import random

# The 'dis' module is imported here, but the 'print_instructions' function is not used in this code.
from dis import print_instructions

# ASCII art representations for Rock, Paper, and Scissors
rock = ('''
    _______
---'    ____)
       (_____)
       (_____)
       (____)
- --._(___)
''')
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Storing the options (Rock, Paper, Scissors) in a list
options = [rock, paper, scissors]

# Prompting the player to choose Rock (0), Paper (1), or Scissors (2)
playerDecision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
# Displaying the player's chosen option
print(f"{options[playerDecision]}")

# Generating a random number between 0 and 2 to represent the computer's choice (Rock, Paper, Scissors)
randomNumber = random.randint(0,2)
# Displaying the computer's choice
print(f"{options[randomNumber]}")

# Checking if it's a tie: the player and computer made the same choice
if playerDecision == randomNumber:
    print("It's a tie!")
# Checking if the player wins (Rock beats Scissors, Paper beats Rock, Scissors beats Paper)
elif ((playerDecision == 0 and randomNumber == 2) or
    (playerDecision == 1 and randomNumber == 0) or
    (playerDecision == 2 and randomNumber == 1) ):
    print(f"You Win!")
# Checking if the player loses (Rock loses to Paper, Paper loses to Scissors, Scissors loses to Rock)
elif ((playerDecision == 0 and randomNumber == 1) or
    (playerDecision == 1 and randomNumber == 2) or
    (playerDecision == 2 and randomNumber == 0) ):
    print(f"You lose!")
# Handling invalid input where the player selects an invalid option
else:
    print("Wrong option! Pick again!")


