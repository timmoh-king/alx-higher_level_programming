#!/usr/bin/node

/*
 * if no arguments are passed to the script, print “No argument”
 * if only one argument is passed to the script, print “Argument found”
 * otherwise, print “Arguments found”
 */

const argv = process.argv.length;

if (argv === 3) {
  console.log('Argument found');
} else if (argv > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
