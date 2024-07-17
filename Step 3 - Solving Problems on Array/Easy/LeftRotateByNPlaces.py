def rotate(arr,k):
    n = len(arr)
    k = k%n
    
    def reverse(start,end):
        while start < end:
            arr[start], arr[end] = arr[end],arr[start]
            start,end = start+1,end-1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)

arr = [1,2,3,4,5,6]
k = 4
rotate(arr,k)
print(arr)