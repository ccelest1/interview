function getMaxPositiveTransactions(transactions) {
    transactions.sort((a, b) => a - b)
    let acc = 0
    let index = transactions.length - 1
    let count = 0
    while (
        acc >= 0 && index >= 0
    ) {
        acc += transactions[index]
        if (acc <= 0) {
            break
        }
        index--
        count++
    }
    return count
}

console.log(
    getMaxPositiveTransactions(
        [-20, 3, 0, 1, 2]
    )
)


function getMaxPositiveTransactions2(transactions) {
    transactions.sort((a, b) => b-a)
    let acc = 0
    let index = transactions.length - 1
    let count = 0
    while (
        index<transactions.length && acc>0
    ) {
        acc += transactions[index]
        index++
        count++
    }
    return count
}

console.log(
    getMaxPositiveTransactions(
        [-20, 3, 0, 1, 2]
    )
)
