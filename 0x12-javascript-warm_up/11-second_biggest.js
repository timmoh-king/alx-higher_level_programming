#!/usr/bin/node

/*
 * Write a script that searches the second biggest integer in the list of arguments
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */
const argv = process.argv;
let temp = 0;

if (!argv || argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 0; i < (argv.length - 1); i++) {
    for (let j = 0; j < (argv.length - 1 - i); j++) {
      if (argv[j] > argv[j + 1]) {
        temp = argv[j];
        argv[j] = argv[j + 1];
        argv[j + 1] = temp;
        console.log(temp);
      }
    }
  }
}
