# Lesson 5
# In this lesson, we are learning how to solve the following problem:
    
# The program takes 2 user inputs:
#     1. The amount of money you started with
#     2. A string composed of 'b' and 'c'

#     Example: "bcbcbc" contains 3 big cookies and 3 normal cookies

networth = float(input("Enter the amount of money that you have: "))
entered = str(input("Enter the sequence of b's and c's with b's meaning big cookies and c's meaning normal cookies: "))
normal = entered.count("c")
big = entered.count("b")

amount = normal+big
norcost = 0.75*normal
bigcost = 1.25*big 
total = norcost+bigcost
if total>networth:
    print("You dont have enough brookie")
else: 
    print(f"The number of cookies sold is {amount}")
    print(f"The total profits made in total is {total}")
