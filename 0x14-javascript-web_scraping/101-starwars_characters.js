#!/usr/bin/node
// prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = "Return of the Jedi"
// Display one character name by line in the same order of the list
// 'characters' in the /films/ response
const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

function helpReq (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).name);
    helpReq(arr, i + 1);
  });
}

request(URL + movieId, function (err, data, body) {
  if (err) {
    console.log(err);
  }
  const charac = JSON.parse(body).characters;
  helpReq(charac, 0);
});
