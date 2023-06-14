#!/usr/bin/node

/*
 * Write an empty class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if ((h == 0 || isNaN(h)) || (w == 0 || isNaN(w))) {
      return {};
    }
  }
}
module.exports = Rectangle;
