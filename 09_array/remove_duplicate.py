def removeDuplicate(arr):
    st = set(arr)  #retrun the object 
    return sorted(list(st))

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
uniqueArr = removeDuplicate(arr)
print(uniqueArr)
for i in uniqueArr:
    print(i)