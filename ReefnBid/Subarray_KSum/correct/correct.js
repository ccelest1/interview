function findLongestSubarray(input_array, target) {
    // in order to keep track of longest array we should establish the length counter and the subarray that will be considered longest

    let maxLen = 0;
    let maxsubarray = [];

    // iterate through with start as variable
    for (let start = 0; start < input_array.length; start++) {

        // initialize variable to store current subarray's sum (start -> end)
        let sum = 0;
        //initialize second loop starting from first iterable
        for (let end = start; end < input_array.length; end++) {
            // tracking sum of current subarray
            sum += input_array[end]

            // length of subarray is the index of it's end - index of it's start + 1 as its 0 index
            let length = end - start + 1

            //logic to determine if we have found longest subarray
            if (
                //we know that sum of current subarray is less than target and not greater
                // and we know that the length of the given current subarray is greater than that of the last stored maxLen
                sum <= target &&
                length > maxLen
            ) {

                maxLen = length;
                maxsubarray = input_array.slice(start, end + 1)

            }
            // if we find that we have gotten a subarray with a greater sum then we break immediately as we know it's not desired
            if (sum > target) {
                break
            }
        }
    }
    return maxsubarray
}

console.log(
    findLongestSubarray(
        [8, -14, 2, 4, 12, -5],
        5
    )
)
console.assert(
    JSON.stringify(
        findLongestSubarray(
            [-5, 8, -14, 2, 4, 12],
            5
        )
    ) === JSON.stringify(
        [-5, 8, -14, 2, 4]
    ),
    'Test Failed'
)

console.log(findLongestSubarray([1, 2, 3]))

console.assert(
    JSON.stringify(
        findLongestSubarray([1, 2, 3],
            5
        )
    ) === JSON.stringify(
        [2, 3]
    ),
    `Test Failed`
)
