/**
 * @param {Array<number>}  arr
 * @param {number} s
 */

function find_quad(arr, s) {
    if (
        arr.length < 4 ||
        arr.reduce((sum, iter) => sum + iter, 0) < s ||
        arr.length === 0
    ) {
        return []
    }

    // REMEMBER TO SORT!!!!
    arr.sort((a, b) => a - b)

    const N = arr.length

    for (let i = 0; i < N - 3; i++) {
        for (let j = i + 1; j < N - 2; j++) {
            let r = s - (arr[i] + arr[j])
            let low = j + 1
            let high = N - 1
            while (low < high) {
                console.log(low, high)
                let high_low = arr[high] + arr[low]
                if (high_low < r) {
                    low += 1
                } else if (high_low > r) {
                    high -= 1
                } else {
                    let quad = [
                        arr[i], arr[j], arr[low], arr[high]
                    ]
                    return quad
                }
            }
        }
    }
}

console.log(find_quad([2, 7, 4, 0, 9, 5, 1, 3], 20))
