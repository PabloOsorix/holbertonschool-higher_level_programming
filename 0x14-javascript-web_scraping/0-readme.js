#!/usr/bin/node
/*   script that reads and prints the content of a file.
    */
const argv = process.argv[2];
const fs = require('fs');

fs.readFile(argv, 'utf8', error);
function error (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}
