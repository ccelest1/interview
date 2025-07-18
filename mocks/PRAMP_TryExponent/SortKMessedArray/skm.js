/**
 *
 * @param {object[number]} arr
 * @param {number} k
 * @returns

Performing insertion sort as we only have a few elements involved in the sorting process vs merge sort which would be used for several elements in a list

Simple Solution = sort whole array
Worst case TC = O(n * log(n)), n being input array size
Does not use the fact that array is k sorted

- Use insertion sort that sorts correct order in O(N*K) time, O(n) space
 */

function kMessedArray(arr, k) {
    for (let i = 0; i < arr.length; i++) {
        // store current element
        let curr = arr[i]
        // store index of previous element
        let prev = i - 1
        while (prev >= 0 && arr[prev] > curr) {
            // perform swap
            // i = i-1
            arr[prev + 1] = arr[prev]
            // then shift back to perform value comparison
            prev -= 1

            // loop continues until we get to beginning or we don't find elements smaller than current element stored
        }
        // place element in correct position
        arr[prev + 1] = curr
    }
    return arr
}

if (JSON.stringify(kMessedArray(
    [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2
)) === JSON.stringify([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) {
    console.log('correct')
} else {
    console.log('false')
}
