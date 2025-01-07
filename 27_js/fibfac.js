//Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

function fact(n) {
    if (n < 0) {
        return undefined; 
    } else if (n === 0 || n === 1) {
        return 1; 
    } else {
        return n * fact(n - 1); 
    }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

console.log(fact(1)); 
console.log(fact(2)); 
console.log(fact(3)); 
console.log(fact(4)); 

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

function fib(n) {
    if (n < 0) {
        return undefined; 
    } else if (n === 0) {
        return 0; 
    } else if (n === 1) {
        return 1; 
    } else {
        return fib(n - 1) + fib(n - 2); 
    }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

console.log(fib(1)); 
console.log(fib(2)); 
console.log(fib(3)); 
console.log(fib(4)); 
//=================================================================
