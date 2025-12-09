# Lesson 9
# In this lesson, we are learning how to create a Rock Paper Scissors game against an AI.

# Create a program that takes one inputs of Rock, Paper, or Scissors to simulate a 1v1 rock paper scissors game between a human player vs AI.

# ### Problem Overview

# Take a single input of rock, paper, or scissors then compare it to the randomly chosen option for the CPU.

# ### You will learn:

# - How to use membership operators with the ```set``` datatype
# - How to use a while loop to validate user inputs
# - How to use ```choice()``` function from the random module

import random

valid_moves = {"rock", "paper", "scissors"}  # strings must be quoted

move = input("Enter one of the valid moves, rock, paper, scissors or enter end to end the game: ").strip().lower()

while move != "end":  # "end" must be in quotes
    if move in valid_moves:   # this check was missing
        cpu_move = random.choice(list(valid_moves))
        print("CPU chose:", cpu_move)

        if move == cpu_move:
            print("tie")
        elif (move == "rock" and cpu_move == "scissors") or \
             (move == "scissors" and cpu_move == "paper") or \
             (move == "paper" and cpu_move == "rock"):
            print("You win!")
        else:
            print("you lose")
    else:
        print("invalid input")
        
    move = input("Enter one of the valid moves, rock, paper, scissors or enter end to end the game: ").strip().lower()
