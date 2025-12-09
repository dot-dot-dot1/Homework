# Lesson 20
def perfect_num(num):
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num //i:
                divisors.append(num//i)
    return sum(divisors) == num

total = 0
for n in range(2, 10001):
    if perfect_num(n):
        total += n
print(total)