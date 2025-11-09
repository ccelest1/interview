/*
    Implement debounce function for handling user input
    events like typing
    + corresponding unit test

    - used for search boxes, window resizing, scroll events, auto save features, api rate limiting

    - in searching -> we wait till user is done typing for executing final search
 */

// debounce fn takes in 2 args being: callback function and duration in milliseconds `wait`
function debounce(callback, wait) {
    let timeoutId; // executed once

    return (...args) => {
        // clear out any pre-existing timeout
        clearTimeout(timeoutId)

        // schedule a new timeout based on amount of time indicated= by wait arg
        timeoutId = setTimeout(() => {

            // with expiring timeout, call `callback` fn with `apply` and feed it given arguments
            // common pattern for passing args, callback doesn't use this
            callback.apply(null, args);

        }, wait);
    }
}

// unit test
let callCount = 0;
const debouncedfn = debounce(() => callCount++, 100); debouncedfn();
debouncedfn();
debouncedfn();
setTimeout(() => {
    console.assert(
        callCount === 1,
        'Only call once after delay'
    )
}, 150);
/*

Debounce function returns a function

const debouncedFunction = debounce(
    function(){...}, 250
)

initial function `debouncedFunction` = stuff one is trying to do
`debounce` function = piece of factory machinery that warps around function causing behavior
Function returned is augmented

- If user moves mouse around for 1 second, cycle repeats and once they stop moving, cycle stops
    * 250 ms elapses -> timeout fires -> code is ran
*/

function debounce2(callback, wait) {
    let timeoutId;

    // use function not arrow fxn here
    // x return (...args)=>{} (preserve outer this)
    // below is dynamic
    return function (...args) {
        const context = this;
        clearTimeout(timeoutId)
        timeoutId = setTimeout(() => {
            callback.apply(context, args)
        }, wait)
    }
}

const obj = {
    name: 'Alice',
    greet: debounce2(function () {
        console.log(
            `Hello, ${this.name}`
        )
    }, 500)
}

obj.greet();

/*

Debounce resets timer everytime function is called
Only executes after you stop calling it for full wait period

 */
