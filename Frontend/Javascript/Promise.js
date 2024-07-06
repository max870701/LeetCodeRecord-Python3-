// 1. How to construct a basic Promise
const promise = new Promise((resolve, reject) => {
    resolve(value)
    reject(reason)
})

promise.then((value) => {
    console.log(value)
}, (reason) => {
    console.log(reason)
})
// 2. Apply a Promise in the return in an asynchronous function
function requestData(url) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (url === "target") {
                resolve("This is the target url.")
            } else {
                reject("Not the target url.")
            }
        }, 3000)
    })
}

requestData("target")
    .then((res) => {
        console.log(res)
    })

requestData("not target")
    .catch(e => console.log(e))

// 3. Explain how to use Promise.race method and then Implement Promise.race method

// 4. Explain how to use Promise.all and then Implement Promise.all method
const promise1 = Promise.resolve(3)
const promise2 = 42
const promise3 = new Promise((resolve, reject) => {
    setTimeout(resolve, 100, "foo")
})

Promise.all([promise1, promise2, promise3])
    .then((values) => {
        console.log(values)
    })


function promiseAll(promises) {
    // basic case
    if (!Array.isArray(promise)) {
        return new TypeError("Arguments must be an array.")
    }

    if (promise.length === 0) {
        return Promise.resolve([])
    }

    const outputs = []
    let resolveCounter = 0

    return new Promise((resolve, reject) => {
        promises.forEach((currentPromise, index) => {
            currentPromise()
                .then((value) => {
                    outputs[index] = value
                    resolveCounter++
                    if (resolveCounter === promises.length) {
                        resolve(outputs)
                    }
                })
                .catch(reject)
        })
    })
}

// 5. Explain the relationship between async/await (ES7 feature) and Promise
//    async <-> Promise.resolve()
//    await <-> .then()

// 6. While using async/await, how can we catch the error message?
// Ans: We can use try/catch
const myName = async () => "Ray"

try {
    console.log(await myName())
} catch(e) {
    console.log(e)
}