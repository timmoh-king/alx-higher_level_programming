#!/usr/bin/node

/*
 * My number: <first argument converted in integer>
 */
const argv = Math.trunc(Number(process.argv[2]));

if (isNaN(argv)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv}`);
}
