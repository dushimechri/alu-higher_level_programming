#!/usr/bin/node
const arguments = process.argv.slice(2);
if (arguments.length === 1 || arguments.length === 0) {
  console.log(0);
}
else {
  let sorted = arguments.map(Number).sort((a, b) => b -a);
  console.log(sorted[1]);
}
