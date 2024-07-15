def isArmstrong(num):
    k = len(str(num))
    sum = 0
    n = num
    while n > 0:
        ld = n % 10
        sum += ld ** k
        n = n // 10
    return sum == num

number = 153
if isArmstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
