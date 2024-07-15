import math

def findDivisors(n):
    divisors = []
    sqrtN = int(math.sqrt(n))
    for i in range(1, sqrtN + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


number = 12
divisors = findDivisors(number)
print("Divisors of", number, "are:", end=" ")
for divisor in divisors:
    print(divisor, end=" ")
print()
