arr = [92, 11, 2, 34, 56, 9, 34]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print('Sorted Array : ', arr)
print('Largest Element : ', arr[-1])