#!/usr/bin/node
//  script that display the status code of a GET request.
const request = require('request');
const argv = process.argv[2];

request(argv, (err, response) => {
  if (err) console.log(err);
  console.log('code:', response.statusCode);
});
