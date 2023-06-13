#!/usr/bin/node

/*
 * Write a script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 */
const argv = Math.trunc(Number(process.argv[2]));

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(argv));
