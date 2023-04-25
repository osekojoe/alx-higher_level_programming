#!/usr/bin/node
// Write string to file.
const fs = require('fs');

try {
  fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err, data) {
    if (err) { console.error(err); }
  });
} catch (err) {
  console.error(err);
}
