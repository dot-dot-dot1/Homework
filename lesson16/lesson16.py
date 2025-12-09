# Lesson 16
# FizzBuzz is counting from 1 to 50 and outputing the number; however, certain numbers will output fizz, buzz or fizzbuzz.
# - if the number is a multiple of three: print 'Fizz',
# - if the number is a multiple of five: print 'Buzz',
# - if they are multiples of both: print 'FizzBuzz'
# - otherwise print the number

# ### You will learn:

# - ```range()``` to generate an iterable sequence of integers
# - Use the modulus operator
# - Use a for loop on an iterable sequence


for i in range(1,51):
    if i % 3 ==0  and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz") 
    elif i % 5 == 0:
        print("Buzz")
print(i)
    