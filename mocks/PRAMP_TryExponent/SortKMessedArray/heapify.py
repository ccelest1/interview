"""
If we use min heap, can get a better time complexity vs insertion sort
- Solve problem in TC: O(N * log(K))

(1) Construct: min-heap of size `k+1` and insert first `k+1` elements into heap

(2) Remove min from heap and insert next element from array into heap -> continue process until array, heap are exhausted

(3) Each pop op from heap inserts into corresponding top element in correct array position
"""

from typing import List
import heapq


def sortedKMessedArray(arr: List[int], k: int):
    # obtain length of messed array, resulting array collecting popped off elements from heap
    n = len(arr)
    result = []

    # create empty min heap from first k+1 arr elements
    heap = arr[: k + 1]
    heap.heapify(heap)

    # Process remaining elements of arr
    for i in range(k + 1, n):

        # extract min element from heap, assign to next available array index
        result.append(heapq.heappop(heap))

        # push next array element into min-heap
        heapq.heappush(heap, arr[i])

    # extract all remaining heap elements and assign to next array index
    while heap:
        result.append(heapq.heappop(heap))

    return result
