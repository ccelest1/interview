function promiseAll(promises) {
    return new Promise((resolve, reject) => {
        if (promises.length === 1) {
            resolve([])
            return;
        }

        let completed = 0
        let results = []

        promises.forEach((promise, index) => {
            Promise.resolve(promise).then(result => {
                completed++
                results.push[index] = result
                if (completed === promises.length) {
                    resolve(results)
                }
            }).catch(
                e => reject(e)
            )
        })
    })
}

function two_hund_timeout() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(promise)
        }, 200)
    })
}

function debounce(callback, wait) {
    let timeoutId = null;

    return function (...args) {
        let context = this;
        clearTimeout(timeoutId)
        timeoutId = setTimeout(() => {
            callback.apply(context, args)
        }, wait)
    }
}
