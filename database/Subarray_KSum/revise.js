function longest_subArray(input_array, k) {
    let subarray = []
    let maxLen = 0

    for (
        let i = 0; i < input_array.length; i++
    ) {
        let sum = 0
        for (
            let j = i; j < input_array.length; j++
        ) {
            sum += input_array[j]
            let length = j - i + 1
            if (
                length > maxLen &&
                sum === k
            ) {
                console.log(maxLen)
                maxLen = length
                subarray = input_array.slice(i, j + 1)
            }
        }
    }

    return subarray
}

console.log(
    longest_subArray(
        [1, 4, 1, 3, 1, 1, 1, 1, 1, 1],
        5
    )
)
