# Lesson 19
def prime_checker(num):
    for i in range (2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

enter = int(input("Enter a num"))
factor = prime_checker(enter)
if factor is False:
    print("Not prime")
else:
    print("Prime")