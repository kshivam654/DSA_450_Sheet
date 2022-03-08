def largestContiniouSum(arr):
    cur_sum = arr[0]
    cur_sum_soFar = arr[0]
    for i in range(len(arr)):
        cur_sum = max(arr[i], cur_sum+arr[i])
        cur_sum_soFar = max(cur_sum_soFar, cur_sum)
    return cur_sum_soFar
print(largestContiniouSum([-2, -3, 4, -1, -2, 1, 5, -3]))

