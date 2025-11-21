function two_second_call() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('resolved')
        }, 2000)
    })
}


async function second_async() {
    console.log('starting call')
    let result = await two_second_call()
    console.log(result)
}

second_async()
