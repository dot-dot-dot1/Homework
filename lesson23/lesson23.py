# Lesson 23
# Given random amount of numbers, determine the average of the inputs.

numbers = []
active = True
while active:
    num = (input("Enter a number or enter \"leave\" to leave "))
    if num.lower() == "leave":
        active = False
    else:
        numbers.append(int(num))

adding = sum(numbers)
print(adding)
