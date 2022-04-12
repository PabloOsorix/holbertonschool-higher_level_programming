#!/usr/bin/node

const argv = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(argv, string, 'utf8', (err) => {
  if (err) throw err;
});
