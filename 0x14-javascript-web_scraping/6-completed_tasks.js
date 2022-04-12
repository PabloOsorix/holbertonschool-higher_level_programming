#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, (err, response, body) => {
  if (err) console.log(err);
  const content = JSON.parse(body);

  for (let i = 0; content[i] != null; i++) {
    if (!dict[content[i].userId]) {
      if (content[i].completed === true) {
        dict[content[i].userId] = 1;
      } else {
        dict[content[i].userId] = 0;
      }
    } else {
      if (content[i].completed === false) {
        continue;
      }
      dict[content[i].userId] = dict[content[i].userId] + 1;
    }
  }
  console.log(dict);
});
