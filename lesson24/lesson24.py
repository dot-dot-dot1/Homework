# Lesson 24
# Until the user inputs the string ```X```, accept name in a string. After the ```X``` is inputted, output the name that was the longest.
enter = True
highest = ""
while enter:
    entering = input("Enter a string and if you input '''X''' then i will find the longest one u inputed")
    if entering == "'''X'''":
        enter = False
    else:
        if len(entering) > len(highest):
            highest = entering
    
print(f"The longest string was {highest}")
        
