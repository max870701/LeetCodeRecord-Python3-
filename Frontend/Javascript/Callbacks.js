// 1. What is the Callback function?
// A: A callback function is a function passed into another function as an argument, 
//    which is then invoked inside the outer function to complete some kind of routine or action.

// 2. Give me an example of callback function.
function greet(name, callback) {
    console.log('Hello ' + name);
    callback();
}

// Define the callback function
function displayMessage() {
    console.log('This message is shown after the greeting!');
}

// Call the function with the callback
greet('Alice', displayMessage);

// 3. How to combine a callback function in an asynchronous function? Give me an example.
const request = require('request')

const geocode = (address, callback) => {
    const uri = '' + encodeURI(address) + ''

    request({uri: uri, json: true}, (error, response) => {
        if (error) {

        } else if () {

        } else {
            
        }
    })
    
}

geocode('Taichung', (error, data) => {
    console.log('Error', error)
    console.log('Data', data)
})

// 4. Write a add function with the requirements below.
//    - Define an add function that accepts the correct arguments
//    - Use setTimeout to simulate a 2 second delay
//    - After 2 seconds are up, call the callback function with the sum
//    - Test your work!

const add = (num1, num2, callback) => {
    setTimeout(() => {
        callback(num1 + num2)
    }, 2000)
}

add(1, 4, (sum) => {
    console.log(sum)
}) 