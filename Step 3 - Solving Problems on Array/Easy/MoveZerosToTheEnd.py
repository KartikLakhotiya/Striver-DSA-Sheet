def moveZeros(n: int, a: [int]) -> [int]: # type: ignore
    j = -1
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    if j == -1:
        return a
    for i in range(j+1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    return a


arr = [1, 0, 2, 3, 0, 2, 0, 0, 4, 5, 1]
n = len(arr)
ans = moveZeros(n, arr)
for i in ans:
    print(i, end=" ")
print()
