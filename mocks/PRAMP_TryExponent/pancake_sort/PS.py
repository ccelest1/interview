from typing import List

"""
1 - create def flip(arr: list[int], k: int)
Reverse order of first k elements in array arr
arr = [1, 5, 4, 3, 2]
-> flip(arr) = [2, 3, 4, 5, 1]
i, j = 0, 1
for i, j in arr:
    if arr[i] > arr[j]: flip(arr[i], arr[j])
2- pancakeSort(arr) -> sort and return input array
create a function that performs sorting
sorting algorithm
def panckaeSort():
    flip(arr, k) -> sorted algorithm
we need to find out the number of flip operations needed
to get the array in sorted order
invoke flip(arr, 2) -> ask if before flip if element[0]<alement[1] or vice versa
if element 0 is less than element 1 peforem flip
"""


def pancake_sort(arr: List[int]) -> List[int]:

    # function flip() rev order of 1st k elements
    # 2, 3, 4, 5
    def flip(arr: List[int], k: int):
        i = 0
        j = k - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            if i == j:
                break
        return arr

    # define pancakgeSort()
    def pancakeSort(arr):
        # increment in reverse order while performing flips
        N = len(arr)

        # perform flip ops in reverse order, find element that is largest
        for curr_size in range(N, 1, -1):
            max_idx = 0
            for i in range(curr_size):
                if arr[i] > arr[max_idx]:
                    max_idx = i

            # if it's not at end of current window observed
            if max_idx != curr_size - 1:
                # if it's not in ideal placement at first element
                if max_idx != 0:
                    # flip to get to ideal
                    flip(arr, max_idx + 1)
                flip(arr, curr_size)

        return arr

    return pancakeSort(arr)


print(pancake_sort([1, 5, 4, 3, 2]))
