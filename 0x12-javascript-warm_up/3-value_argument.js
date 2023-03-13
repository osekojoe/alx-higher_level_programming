#!/usr/bin/node
if (process.arg[2] === undefined) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
