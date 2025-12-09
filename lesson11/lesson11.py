# Lesson 
# A cartesian plane can be divided into 4 quadrants based on this image:

# ![quadrants](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4a4xLspgRHPa5dCoG6i8kO_SZsLVyWG90Sw&s)

# A single point on a cartesian plane is composed of two values (x-coordinate, y-coordinate).

# If the x-value is positive, the point can only be in either 1 or 4 quadrant.
# If the y-value is positive, the point can only be in either 1 or 2 quadrant.

# By combining the signs of both coordinates, we can determine where the point lies.

# ### Problem Overview

# Given a single input containing a x-coordinate and a y-coodinate, determine which quadrant the value falls under.

# ### You will learn:

# - How to use ```.split()``` method to create a list from a string
# - How to use ```map()``` function to help us turn values in a list to integers
# - How to use variable unpacking

cordinate = input("Enter the cordinates of the x and y axis with one space in between")
cord_list = cordinate.split(" ")
x, y = map(int, cord_list)
if x > 0 and y > 0:
    print("In quad 1")
elif x<0 and y>0:
    print("in quad 2")
elif x<0 and y<0:
    print("in quad 3")
else:
    print("In quad 4")