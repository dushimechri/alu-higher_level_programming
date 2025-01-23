#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 1 || args.length === 0) {
	  console.log(0);
} else {
	  const sorted = args.map(Number).sort((a, b) => b - a);
	  console.log(sorted[1]);
}
