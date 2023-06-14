#!/usr/bin/node

/*
 * prints the number of arguments already printed and the new argument value.
 */

exports.logMe = function (item) {
  for (let i = 0; i < item.length; i++) {
    console.log(`${i} : ${item[i]}`);
  }
};
