#!/usr/bin/node

/*
 * Write an empty class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    if ((h > 0 && !isNaN(h)) && (w > 0 && !isNaN(w))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
