#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const file = process.argv[3];

request(URL, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
