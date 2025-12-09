# Lesson 8
# Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups based on the results of games as follows:

# - if a player wins 5 or 6 games, they are placed in Group 1
# - if a player wins 3 or 4 games, they are placed in Group 2
# - if a player wins 1 or 2 games, they are placed in Group 3
# - if a player does not win any games, they are eliminated from the tournament.

# Write a program to determine which group a player is placed in.

# ### Problem Overview

# Given 6 string inputs of either ```W``` or ```L```, we are to determine which group they fall under for the tournament.

# ### You will learn:

# - How to use a for-each loop in Python
# - How to use the ```range()``` function in Python
# - How to create meaningful conditional statements

games = 0
score = []
while games < 6:
    result = input("Enter either W or L to signify win or loss: ").strip().upper()
    result = result.upper()
    if result == "W":
        score.append("W")
        games+=1
    elif result == "L":
        games+=1
    else:
        print("Invalid input")

wins = score.count("W")
    
if wins >= 5:
    print("Your in group 1")
elif wins >= 3:
    print("Your in group 2")
elif wins >= 1:
    print("Your in group 3")
else:
    print("Your gone")





