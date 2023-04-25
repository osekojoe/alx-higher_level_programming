#!/usr/bin/node
// prints the number of movies where the character
// 'Wedge Antilles' is present.

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, data, body) {
  if (err) {
    console.log(err);
  }
  const nmovies = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(nmovies);
});
