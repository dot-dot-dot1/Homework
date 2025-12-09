# Lesson 7
# In this lesson, we are learning how to solve the following problem:
    
# Create a program that simulates the ability check from the video game called "Baldur's Gate 3".

# An ability check in Baldur's Gate 3 is determined by first the Difficulty Class (DC). The DC is a number representing how hard a task is. When a player wants to do something uncertain, like jumping a gap or sneaking past guards, the Dungeon Master (DM) sets a DC. The player rolls a 20-sided die (D20) and adds modifiers from their character to the roll. If the total meets or beats the DC, the action succeeds. If not, it fails. The D20 introduces randomness, making even skilled characters sometimes fail in challenging situations, adding excitement to the game.

# The program should take in a single integer value representing the DC then randomly roll a value from 1 to 20 inclusively. Determine if the player was successful at succeeding the ability check.

# ### You will learn:

# - How to use ```randrange()``` function from the random module in Python
# - How to construct a simple binary conditional statement
import random
while True:
    dc = int(input("Enter the DC or enter 21 to end the game: "))
    if dc == 21:
        print("Ended game")
        break
    else:
        random = random.randrange(1,21)
    if dc > random:
        print(f"Failed, you rolled a {random}")
    else:
        print(f"Succeded, you rolled a {random}")
