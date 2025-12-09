# Lesson 13
# February 18 is a special date for the CCC this year.

# Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18.

# - If the date occurs before February 18, output the word Before.
# - If the date occurs after February 18, output the word After.
# - If the date is February 18, output the word Special.

# ### You will learn:

# - How to write effective conditional statements
month = int(input("Enter the month in numbers"))
day = int(input("Enter the day in numbers"))
if month == 2:
    if day == 18:
        print("Its today")
    elif day>18:
        print("Its passed")
    else:
        print("Not yet")
elif month>2:
    print("its passed")
else:
    print("Not yet")