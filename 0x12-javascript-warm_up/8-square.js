#!/usr/bin/node

/*
 * Write a script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 */
const argv = Math.trunc(Number(process.argv[2]));
let x = 0;

if (isNaN(argv)) {
  console.log('Missing size');
} else {
  x = x + argv;
}
for (let i = 0; i < x; i++) {
  let line = '';
  for (let j = 0; j < x; j++) {
    line += 'X';
  }
  console.log(line);
}
