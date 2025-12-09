# Lesson 28

def palindrome(string):
    return string == string[::-1]

enter = str(input("Enter a string "))

if palindrome(enter):
    print(f"{enter}is palindrome")
else:
    print(f"{enter} is not a palindrome")

