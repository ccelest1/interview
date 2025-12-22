/**
 * implement custom version of Promise.all() from scratch
 * @param {} promise


Return a new promise that only resolves once each of values in array have resolved and reject if any of the promises reject

Executor function given to function keeps track of results as each promise resolves and keep track of number of promises that have resolve

- Use Cases: load several data sources for dashboard

Arrow functions in promiseAll fn
Promise((resolve, reject)=>{
}

.forEach((promise, index)=>{
}

.then((result)=>{
})
 */

function promiseAll(promises) {
    return new Promise((resolve, reject) => {
        if (promises.length === 0) {
            resolve([])
            return;
        }

        const results = [];
        let completed = 0;

        /*

        forEach iterates over list of values and calls the `then` method on each of them, add result to results list as they resolve

        */
        promises.forEach((promise, index) => {
            Promise.resolve(promise).then(result => {
                // adding to results array incrementally
                // Promise.all maintains order of results from promises provided as input -> Need to know index of promise in order to place it correctly in results list (use index)
                results[index] = result;
                completed += 1
                if (completed == promises.length) {
                    resolve(results)
                }
            }).catch(e => reject(e))
        });
    });
}
