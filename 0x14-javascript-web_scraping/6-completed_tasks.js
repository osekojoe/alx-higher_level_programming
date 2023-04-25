#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, data, body) {
  if (err) {
    console.log(err);
  }
  const dict = JSON.parse(body).reduce((acc, elem) => {
    if (!acc[elem.userId]) {
      if (elem.completed) {
        acc[elem.userId] = 1;
      }
    } else {
      if (elem.completed) {
        acc[elem.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(dict);
});
