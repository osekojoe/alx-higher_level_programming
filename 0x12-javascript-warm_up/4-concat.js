#!/usr/bin/node

if (typeof process.argv[2] !== 'undefined' && typeof process.argv[3] !== 'undefined') {
	console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (typeof process.argv[2] + ' is undefined'); {
	console.log(process.argv[2] + ' is undefined');
} else {
	console.log('undefined is undefined');
}
