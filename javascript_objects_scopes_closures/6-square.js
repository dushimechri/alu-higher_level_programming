#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  constructor(size) {
    super(size);
  }
  charPrint(c = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
