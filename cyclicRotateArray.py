def cycliRotate(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    return arr
print(cycliRotate([1,2,3,4,5]))