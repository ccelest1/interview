/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function (n, k) {
    let queue = []
    for (let i = 1; i < n + 1; i++) {
        queue.push(i)
    }
    while (queue.length > 1) {
        let toRemove = k - 1
        while (toRemove > 0) {
            queue.push(queue.shift())
            toRemove--;
        }
        queue.shift()
    }
    return queue.shift()
}
