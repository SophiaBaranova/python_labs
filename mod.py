from math import sqrt, fmod

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