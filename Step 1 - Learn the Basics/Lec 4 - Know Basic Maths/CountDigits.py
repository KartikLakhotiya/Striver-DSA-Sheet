import math


def countDigits(n):
    cnt = int(math.log10(n) + 1)
    return cnt


N = 329823
print("N:", N)
digits = countDigits(N)
print("Number of Digits in N:", digits)