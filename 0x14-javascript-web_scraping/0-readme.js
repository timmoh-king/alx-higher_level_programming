#!/usr/bin/node

/*
 * Write a script that reads and prints the content of a file
 */

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, (err, data) => {
  if (err) throw err;

  console.log(data.toString());
});
