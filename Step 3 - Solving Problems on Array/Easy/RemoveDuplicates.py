from typing import List
def removeDuplicates(arr:List[int]) -> int:
    i=0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1

arr = [1,1,2,2,3,4,4,5]
k = removeDuplicates(arr)
print("The Array after removing duplicate elements is : ")
for i in range(k):
    print(arr[i], end=" ")