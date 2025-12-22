# 11/05/25

## [Longest Subarray with K Sum](https://www.geeksforgeeks.org/dsa/longest-sub-array-sum-k/)

### Problem
- Given array arr[] (size `n`) with integers, find longest subarray with sum = `k`
    * If there is no subarray with sum == k, return 0

### Analysis
- Input: Given an input array:`arr[]` and target sum of `k`
- Output: Return longest subarray

- Algo Process
    - Restate Problem
        * Need to find longest collection of numbers that will get us to target value of k

    - Goal of Function
        * Return longest subarray given list of integers and target value

    - Types
        * list[int], int

    - Assertions and Assumptions
        * Can't return an array whose sum is larger than target

    - Edge Cases (regardless of assertions, assumptions)
        * Consider negative numbers
        * Instances where we don't have a subarray that sums up to target => 0


#### Example \#1
```js
let arr[] = [10, 5, 2, 7, 1, -10], let k = 15
// output is entire array
```

#### Example \#2
```js
arr[] = [-5, 8, -14, 2, 4, 12], k = -5
// output = [-5, 8, -14, 2, 4]
```
#### Example \#3 
```js
arr[] = [10, -10, 20, 30], k = 5
// output => 0 as a subarray with that kSum is impossible
```

### Preliminary Solution
- __Time Complexity__:

- __Space Complexity__:

#### _Backside_
- Reflecting on Attempt:
