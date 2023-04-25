#!/usr/bin/node
// Reads and prints the content of a file.
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
