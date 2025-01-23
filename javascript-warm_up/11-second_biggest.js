#!/usr/bin/node
const argumentss = process.argv.slice(2);
if (argumentss.length === 1 || argumentss.length === 0) {
  console.log(0);
}
else {
  let sorted = argumentss.map(Number).sort((a, b) => b -a);
  console.log(sorted[1]);
}
