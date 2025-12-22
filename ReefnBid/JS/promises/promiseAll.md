# [Implementing Promise.all()](https://medium.com/@copperwall/implementing-promise-all-575a07db509a)

- Promise.all = static method on Promise object that takes list of items and returns a promise that resolves w/ list containing values of all resolved vals in input list
    * If any values are rejected promises, returned promise will also be rejected -> (returned) rejection message of 1st that failed
    * __Helpful__: Run several promises concurrently and wait until all have been fulfilled prior to progressing

- Example: using promises directly -> make several concurrent reqs to various API endpoints and wait until they are completed to operate on responses
    ```js
    Promises.all([
        fetch('/api/a'),
        fetch('/api/b'),
        fetch('/api/c')
    ]),then([responseA, responseB, responseC] => {
        // use responses from all 3 async reqs
    })
   ```

- Use Promise.all in async if you want several function calls to operate concurrently instead of sequentially
    * Wait for sum time of requests (inefficient)
    ```js
    async function doSomeThings(){
        const result1 = await fetch('/api/a');
        const result2 = await fetch('/api/b');

        return{
            ...result1,
            ...result2
        }
    }
    ```
    * both requests are initiated at the same time -> wait for max instead of sum for requests times to run
    ```js
    async function doSomeThings(){
        const resultPromise1 = fetch('/api/a');
        const resultPromise2 = fetch('/api/b');

        try{
            const[result1, result2] = Promise.all([
                resultPromise1,
                resultPromise2
            ]);
        }catch(e){
            debug('There was an error', e.message)
        }

        return{
            ...result1,
            ...result2
        }
    }
    ```
