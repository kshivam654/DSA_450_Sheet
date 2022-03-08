def fun(arr):
    j = 0
    n = len(arr)
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print(arr)
print(fun([-12, 11, -13, -5, 6, -7, 5, -3, -6]))