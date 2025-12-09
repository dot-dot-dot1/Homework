# Lesson 3
# Given a positive integer input representing the number of equal size tiles, we are to determine the following:
# - Construct the square with the largest area possible
# - Output the side length of the square
import math
numoftiles = int(input("Enter the number of tiles "))

side_length = math.isqrt(numoftiles)
print(side_length)