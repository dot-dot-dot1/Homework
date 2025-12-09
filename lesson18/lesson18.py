# Lesson 18
def factor_finder(num):
    factors = [1]
    for i in range (2, int(num**0.5)+1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    factors.append(num)
    return sorted(factors)

enter = int(input("Enter a number"))
factors = factor_finder(enter)
print(factors)