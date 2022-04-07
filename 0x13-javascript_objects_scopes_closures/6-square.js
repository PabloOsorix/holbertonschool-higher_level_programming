#!/usr/bin/node
//  add method charPrint to Square class.
const squareOne = require('./5-square');
class Square extends squareOne {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
