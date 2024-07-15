def palindrome(n):
    revNum = 0
    dup = n
    while n > 0:
        ld = n % 10
        revNum = (revNum * 10) + ld
        n = n // 10
    if dup == revNum:
        return True
    else:
        return False


number = 4554

if palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
