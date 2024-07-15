#  Pattern 1
#  https://takeuforward.org/pattern/pattern-1-rectangular-star-pattern/

'''
print("Pattern 1 \n")
n = int(input("Enter A Number : "))
for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()
'''


# Pattern 2
# https://takeuforward.org/pattern/pattern-2-right-angled-triangle-pattern/

'''
print("Pattern 2 \n")
n = int(input("Enter A Number : "))
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()
'''

# Pattern 3
# https://takeuforward.org/pattern/pattern-3-right-angled-number-pyramid/

'''
print("Pattern 3\n")
num = 1
n = int(input("Enter A Number : "))
for i in range(5):
    for j in range(i+1):
        print(j+1, "", end="")
    print()
'''

# Pattern 4
# https://takeuforward.org/pattern/pattern-4-right-angled-number-pyramid-ii/

'''
print("Pattern 4\n")
n = int(input("Enter A Number : "))
for i in range(5):
    for j in range(i+1):
        print(i+1, "", end="")
    print()
'''

# Pattern 5
# https://takeuforward.org/pattern/pattern-5-inverted-right-pyramid/

'''
print("Pattern 5\n")
n = int(input("Please Enter a Number : "))
for i in range(n):
    for j in range(n-i):
        print("* ", end="")
    print()
'''

# Pattern 6
# https://takeuforward.org/pattern/pattern-6-inverted-numbered-right-pyramid/

'''
print("Pattern 6\n")
n = int(input("Enter A Number : "))
for i in range(n):
    for j in range(n-i):
        print(j+1, "", end="")
    print()
'''

# Pattern 7
# https://takeuforward.org/pattern/pattern-7-star-pyramid/

print("Pattern 7\n")
n = int(input("Enter a Number: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
