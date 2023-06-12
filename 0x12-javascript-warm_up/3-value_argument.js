#!/usr/bin/node

/*
 * if no arguments are passed to the script, print “No argument”
 * if only one argument is passed to the script, print “Argument found”
 * otherwise, print “Arguments found”
 */

const argv = process.argv;
let results = 0;

argv.forEach(function(element){
	results = results + element;
});

if (argv < 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}