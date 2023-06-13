#!/usr/bin/node

/*
 * Write a script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 */
const argv1 = Math.trunc(Number(process.argv[2]));
const argv2 = Math.trunc(Number(process.argv[3]));

function add (a, b) {
  return (a + b);
}

console.log(add(argv1, argv2));
