#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
function factorial(num1) {
	if (num1 === 0 || num1 === 1 ) {
		console.log(1);
	}
	else {
		console.log(num1 * factorial(num1 - 1));
	}
}
factorial(num1);
