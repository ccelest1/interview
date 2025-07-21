# 07/17/25

## K-messed Array Sort

### Problem
> Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

> Analyze the time and space complexities of your solution.

### Analysis
- Input: two inputs with the 1st being of list[int] and the second of int -> we are told that each element is at most k places away from sorted position
    * Ex:
        - len(arr) = 10, k=2
        - element at index 6 in sorted array is either at 4-8 in messed array

- Output: Return array that is sorted

- Algo Process
    - Restate Problem
        * sort array knowing that messed up elements are off an order of 2 indices

    - Goal of Function
        * get back sorted array

    - Types
        * list[int], int

    - Assertions and Assumptions
        * we are given k as the accurate number of shuffling

    - Edge Cases (regardless of assertions, assumptions)
        * empty arr, identical/duplicate elements


#### Example \#1
```py
input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### Constraints
- `1 <= arr.length <= 100`
- `0 <= k <= 20`

### [Solutions]
- [Simple Solution](skm.js)
    * TC: O(n*k), SC: O(1) -> modifies array in place instead of creating new array
- [Heap Solution](heapify.py)
    * TC: O(N * log(K)), SC: O(K)

### Rationale of Insertion vs Merge Sort
- In this case with a dataset that will be less than or equal to 100 elements, insertion sort is a better sorting algo to employ
    * Insertion sort = faster for small, nearly sorted datasets (as is the case as above)
        - O(n) to O(n^2) [ large, unsorted datasets ]
        - In place sorting algo -> doesn't require extra space proportional to input size
    * Merge sort -> larger, very unsorted datasets
        - Recursively divide array into smaller subarrays -> sort subarrays -> merge sorted subarrays together
        - TC: O(n log n), divide and conquer algo
        - SC: O(n), extra space for storing merged subarrays
