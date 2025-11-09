/**
 input: array of integers, target value
 output: two numbers that add up to the target

    iterate through the array of integers
    for each integer we want to create a dictionary that maps to the integer that would sum up to the target value
    [ 0, 1, 4, 5],  9
               i
    {
    0: 9,
    1: 8,
    4: 5
    }

    return [i, target-i]
 */


const findTwoSum = (arr_input, target) => {
    let tracker = {}
    for (let [index, value] of arr_input.entries()) {
        let remainder = target - value
        if (tracker[remainder] !== undefined) {

            return [
                arr_input[tracker[remainder]], arr_input[index]
            ]

        } else {

            tracker[value] = index
        }
    }
    return tracker
}


const arr_input = [0, 1, 4, 5]
const target = 9

console.log(
    findTwoSum(arr_input, target)
)
