from heapq import heappop
import heapq


def findKthSmallestElement(arr, k):
    heapq.heapify(arr)
    return heapq.nsmallest(k, arr)