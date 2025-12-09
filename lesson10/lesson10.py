# Lesson 10
# A telemarketer can be determined if all of the following statements are true:

# - The first digit is 8 or 9.
# - The second and third digits are the same.
# - The last digit is 8 or 9.

# If all three conditions are met, the phone number is a telemarketer. Otherwise, it is not.

# Write a program to determine if the given last four digits would be a telemarketer or not.

# ### Problem Overview

# Given 4 inputs to represent the last four digits of a number, determine if the call is from a telemarketer

# ### You will learn:

# - How to index a string to look at individual characters
# - How to use nested if statements
# Collect the 4 digits
nums = []
counter = 0
while counter < 4:
    num = int(input("Enter a digit: "))
    nums.append(num)
    counter += 1

if (nums[0] in (8, 9)) and (nums[1] == nums[2]) and (nums[3] in (8, 9)):
    print("Telemarketer")
else:
    print("Not a telemarketer")
