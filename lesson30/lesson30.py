# Lesson 30
# Given a numeric input, create a pattern of string to be outputted to the console.

# ```
# Example Patterns

# N = 5

# 1
# 10
# 101
# 1010
# 10101
# ```

n = int(input("Enter a number to be put in a pattern"))

for i in range (1, n + 1):
    pattern = ""
    for j in range(i):
        if j % 2 == 0:
             pattern += "1"
        else: 
            pattern += "0"
    print(pattern)



