# Lesson 4
# In this lesson, we are learning how to solve the following problem:
    
# You are to create a program that determines how many paint cans we'd need.

# - Each plank of the fence requires one paint can.
# - Your supplier only sells paint cans by the dozen (12) for $14.95. 
# - There are 3 fenced sections, and their length will be denoted by a series of 'F' for each fence plank.

sections = input("Enter the length's of the 3 sections seperated by spaces: ")
sections_list = [float(x) for x in sections.split()]

total = sum(sections_list)
import math
cost = math.ceil(total/12)*14.95




