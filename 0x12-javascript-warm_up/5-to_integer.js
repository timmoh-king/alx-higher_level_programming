#!/usr/bin/node

/*
 * My number: <first argument converted in integer>
 */
const argv = process.argv;

if (!argv[2] || !Math.floor(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
