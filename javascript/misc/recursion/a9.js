/*
 * Fibonacci Recursively
 *
 *
 *
 * */

function fib(n) {
  if (n <= 0) {
    return 0;
  } else if (n === 1) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }

}


// verify
console.log(fib(0) === 0);   // Output: 0
console.log(fib(1) === 1);   // Output: 1
console.log(fib(5) === 5);   // Output: 5
console.log(fib(10) === 55);  // Output: 55
console.log(fib(15) === 610);  // Output: 610
