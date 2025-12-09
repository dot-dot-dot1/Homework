# Lesson 12
# In this lesson, we are learning how to solve the [Triangle Times question](https://dmoj.ca/problem/ccc15j1).

# Given a Triangle:
    
# - If all three angles are 60, it is a _Equilateral_ triangle.
# - If the three angles add up to 180 and exactly two of the angles are the same, it is a _Isosceles_ triangle.
# - If the three angles add up to 180 and no two angles are the same, it is a _Scalene_ triangle.

# ### Problem Overview

# Given 3 angles of a potential triangle, determine the type of the triangle: Equilateral, Isosceles or Scalene.

# ### You will learn:

# - Nested if statements
# - Using sum() function
# - Comparison chaining: ``` a == b == c ```
# - proper use of ```and``` operator in Python


angles = input("Enter the 3 angles: ")
inputs = angles.split(" ")
x, y, z = map(int, inputs)

if x == y == z:
    print("Equilateral")
elif x != y and y != z and x != z:
    print("Scalene")
else:
    print("Isosceles")
