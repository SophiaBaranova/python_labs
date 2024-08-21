from math import sqrt, sin, fmod

def z(x):
    try:
        # calculate z
        z = sqrt(2) / 2 * sin(1 / x) + 1
    except ZeroDivisionError: # if x == 0
        print("invalid x, division by zero")
        return
    else: # if x is valid
        return z

def isDeficient(n):
    if n > 0:
        sum = 1 # sum of proper divisors
        k = int(sqrt(n)) + 1
        # check the numbers from 2 to k
        for i in range(2, k):
            if fmod(n, i) == 0: # if i is a divisor
                if i == n / i: # if n = i^2
                    sum += i # add i to sum
                else:
                    sum += i + n / i # add i and its "couple" to sum
        if n > sum: # if n is deficient
            return True
    return False

x = float(input("enter x to calculate z expression: "))
if z(x):
    print(f"z = {z(x):.2f}")
n = int(input("enter n to check if it is deficient: "))
if isDeficient(n):
    print(f"{n} is deficient")
else:
    print(f"{n} is not deficient")