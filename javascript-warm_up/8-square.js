#!/usr/bin/node
const num = parseInt(process.argv[2]);
const X = 'x'
if (Number.isInteger(num)) {
	let line = X.repeat(num);
	    for (let i = 0; i < num; i++) {
		            console.log(line);
		        }
} else {
	    console.log('Missing size');
}
