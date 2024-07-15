n = int(input("Enter an integer: "))
revNum = 0
while n > 0:
    ld = n % 10
    revNum = (revNum * 10) + ld
    n = n // 10
print("Reversed Number : ",revNum)
                           
                        