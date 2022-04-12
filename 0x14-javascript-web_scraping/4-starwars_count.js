#!/usr/bin/node
/*   script that prints the number of movies where the
character “Wedge Antilles” is present.  */

const request = require('request');
const web = process.argv[2];
let counter = 0;
request(web, (err, response, body) => {
  if (err) console.error(err);
  const json = JSON.parse(body).results;
  for (let i = 0; json[i] != null; i++) {
    for (let j = 0; json[i].characters[j] != null; j++) {
      if (json[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        counter++;
      }
    }
  }
  console.log(counter);
});
