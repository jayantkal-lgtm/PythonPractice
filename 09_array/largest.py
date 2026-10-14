def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max

arr = [10,20,30,40,50,60]

print(largest(arr))