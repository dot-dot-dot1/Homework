# Lesson 22
def fibonacci(n):
    if n in (0,1):
        return n
    a, b = 0,1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


n = int(input("Enter n: "))
print(f"The {n}th Fibonacci number is {fibonacci(n)}")
