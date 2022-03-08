def findMaxMinArray(arr):
    if not arr:
        return None, None
    maxArr, minArr = float('-inf'), float('inf')
    for ele in arr:
        maxArr = max(maxArr, ele)
        minArr = min(minArr, ele)
    return minArr, maxArr