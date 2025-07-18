from typing import List


def sort_k_messed_array(arr: List[int], k: int) -> List[int]:
    for i in range(1, len(arr) - 1):
        curr = arr[i]
        prev_index = i - 1

        while prev_index >= 0 and arr[prev_index] > curr:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1
        arr[prev_index + 1] = curr
    return arr


# debug your code below
print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
