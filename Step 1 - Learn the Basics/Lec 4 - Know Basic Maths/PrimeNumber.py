import math


def checkPrime(n):
    cnt = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = cnt + 1
            if n // i != i:
                cnt = cnt + 1
    if cnt == 2:
        return True
    else:
        return False


n = 1483
isPrime = checkPrime(n)
if isPrime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
