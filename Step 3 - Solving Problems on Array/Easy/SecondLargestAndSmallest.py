def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print('Second Smallest is : ', second_small)
    print('Second Largest is : ', second_large)


arr = [2, 4, 6, 8, 10]
n = len(arr)
getElements(arr, n)
