"""
input: arr:list[int], s:int
output: arr[list], first instance of four numbers in ascending order who sum to s

(1) 2sum -> summation, 4 numbers
keep track of the first instance of 4 numbers that sum to 20


(2) when we do get the 4 numbers, implementing a sorting algo -> ascending sort
sorted(array) -> ascending order

[2, 7, 4, 0, 9, 5, 1, 3], s = 20
             i

{2 -> 18}
[7 -> 13]
[4 -> 16]
...
n -> array
2 sum ->
{ [number] = target - number [remaining]}

edge cases:
[0,0,0], s=10
"""

from typing import List


def find_array_quadruplet(arr: List[int], s: int) -> List[int]:
    sorted_arr = sorted(arr)
    tracker = {}
    # 2 pointers, for appending 2 numbers for the sake of matching
    i, j = 0, len(arr)-1
    output = []
    while i < len(sorted_arr) - 1 and j >0:
        sum_pair = sorted_arr[i] + sorted_arr[j]
        remainder = s - sum_pair
        tracker[remainder] = [sorted_arr[i], sorted_arr[j]]
        if remainder in tracker:
            output.append([sorted_arr[i], sorted_arr[j]])
            output.append(tracker[remainder])
        i += 1
        j += 1
    return output

    # if statement, that matches pairs that sum to s


print(find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20))
