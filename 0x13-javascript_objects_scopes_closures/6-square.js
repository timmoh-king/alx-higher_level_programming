#!/usr/bin/node

/*
 * Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
 */

class Square extends require('./5-square') {
  charPrint (c) {
    if (c === 'undefined' || !c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.height; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
