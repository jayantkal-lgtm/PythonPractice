def getSecondLargest(arr):
    n = len(arr)
    arr.sort()

    for i in range(n-2,-1,-1):
        if arr[i] != arr[n-1]:
            return arr[i]

    return -1

arr = [34, 34, 34, 34, 34, 34]
print(getSecondLargest(arr))