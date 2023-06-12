#!/usr/bin/node

/*
 * if no arguments are passed to the script, print “No argument”
 * if only one argument is passed to the script, print “Argument found”
 * otherwise, print “Arguments found”
 */

const argv = process.argv;
let result = 1;

argv.forEach((val, index) => {
  result = result + index;
});
if (result <= 2) {
  console.log('No Argument');
} else {
  console.log(argv[2]);
}
