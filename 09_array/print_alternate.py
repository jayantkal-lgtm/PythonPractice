def return_alternate_elementofArray(arr):
    alternate = []
    for i in range(0, len(arr), 2):
        alternate.append(arr[i])
    return alternate

arr = [10, 20, 30, 40, 50]
newarr = return_alternate_elementofArray(arr)
print(newarr)

# when print  take as string 
print(" ".join(map(str,newarr)))