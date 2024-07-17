def findElement(arr,num):
    for i,element in enumerate(arr):
        if element == num:
            print("Element found at Index")
            return i
    return -1

arr = [1,2,3,4,5]
num = 3
print(findElement(arr,num))