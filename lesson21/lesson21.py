# Lesson 21
# Given a user input of N, a positive integer greater than 1, determine which number from 1 to N has the most number of factors.

# _You just output one of the number in case of a tie._
def factor_compare(num):
    factors = 0
    highest = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            factors += 1
            if i != num // i:
                factors += 1
    return factors
    
N = int(input("enter a positive integer greater than 1 "))
max_factors = 0
number_with_most_factors = 1
for n in range(1, N + 1):
    factors = factor_compare(n)
    if factors > max_factors:
        max_factors = factors
        number_with_most_factors = n

print(f"The number with the most factors is {max_factors}")
    
    
        