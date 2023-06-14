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

  rotate () {
    let a = this.width
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
    return this.width * this.height * 2;
  }
}
module.exports = Rectangle;
