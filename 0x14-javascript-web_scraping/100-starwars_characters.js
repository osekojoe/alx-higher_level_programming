#!/usr/bin/node
// prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = "Return of the Jedi"
// Display one character name by line
const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + movieId, function (err, data, body) {
  if (err) {
    console.log(err);
  }
  JSON.parse(body).characters.forEach(function (url, callback) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
