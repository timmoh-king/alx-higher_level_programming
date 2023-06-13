#!/usr/bin/node

/*
 * Write a script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 */

const argv = Math.trunc(Number(process.argv[2]));
let x = 0;

if (isNaN(argv)) {
  console.log('Missing number of occurrences');
} else {
  x = x + argv;
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
