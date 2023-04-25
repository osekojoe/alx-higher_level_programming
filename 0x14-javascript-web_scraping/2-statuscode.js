#!/usr/bin/node
// display the status code of a GET request.

require('request').get(process.argv[2], function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ' + data.statusCode);
  }
});
