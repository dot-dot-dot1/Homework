# Lesson 25
# Given a positive integer greater than 1, we are to determine the largest [prime factor](https://www.mathsisfun.com/prime-factorization.html) of the integer.
def prime_factor(num):
    largest = None
    while num % 2 == 0:
        largest = 2
        num //= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            largest = i
            num //= i
        i += 2
    if num > 2:
        largest = num
    return int(largest)
n = int(input("Enter a number greater than 1: "))
print(f"The largest prime factor of {n} is {prime_factor(n)}")
