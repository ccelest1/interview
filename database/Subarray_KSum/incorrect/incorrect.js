/**
    find longestSubarray
     - input: array, value
     - output: longest subarray that has sum <= given value
        * include a unit test

    input_array = [1,4,5,6,8]
    value = 10

    [1,4,5,6,8] -> [1,4,5]
    [1,1,4,5,6,8] -> [1,1,4,5]
         i
    .sort() -> array prior to finding longest subarray
 */


function findLongestSubarray(input_array, value) {
    input_array.sort((a, b) => a - b)
    let return_array = []
    let sum = 0
    for (let num of input_array) {
        if (sum + num <= value) {
            return_array.push(num)
            sum += num
        } else {
            break
        }
    }
    return return_array
}


const input_1 = [1, 8, 4, 6, 5]
const target_1 = 10

console.log(
    findLongestSubarray(
        input_1, target_1
    )
)
