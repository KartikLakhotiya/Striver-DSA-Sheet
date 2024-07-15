def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr1 = [23, 67, 45, 23, 54, 23, 53, 12]
bubbleSort(arr1)
print("Sorted Array:")
for i in range(len(arr1)):
    print("%d" % arr1[i], end=" ")
