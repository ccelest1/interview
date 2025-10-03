function cpus(capacities) {
    let res = []
    capacities.sort((a, b) => a - b)

    for (let capacity of capacities) {
        let options = [
            capacity,
            capacity + 1,
            capacity - 1
        ]
        for (let option of options) {
            if (option >= 1 && !res.includes(option)) {
                res.push(option)
                break
            }
        }
    }

    return res.sort((a, b) => a - b).length
}

let example = [1, 1, 4, 4, 1, 4]
let expected = 5

console.log(cpus(
    example
))

console.log(JSON.stringify(cpus(example)) === JSON.stringify(expected))
