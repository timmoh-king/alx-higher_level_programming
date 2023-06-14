#!/usr/bin/node

/*
 * Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      super.print();
    } else if (c === '') {
      super.print();
    } else {
      super.charPrint('C');
    }
  }
}

module.exports = Square;
