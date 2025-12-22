def find_largest_subarray_sum(arr, target):
    """
        # BASE CASES
        IF NOT ARR, IF sum(arr) < target

        # iterate using 2 pointer approach, i and j
        # initialize max_length
        # then in second iteration -> we will ask if length is
        # in range, if the current sum == target
    ​
        # return largest net subarray
    """
    max_subarray = []
    max_length = 0
    N = len(arr)
    if len(arr) == 0 or sum(arr) < target:
        return max_subarray

    for i in range(0, N):
        current_sum = 0
        for j in range(i, N):
            current_sum += arr[j]
            length = j - i + 1
            if length > max_length and current_sum == target:
                max_length = max_length
                max_subarray = arr[i : j + 1]
            if current_sum > target:
                break
    return max_subarray


print(find_largest_subarray_sum([1, 9, 4, 2, 4], 10))
