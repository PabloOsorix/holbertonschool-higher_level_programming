#!/usr/bin/node
/*  script that gets the contents of
a webpage and stores it in a file.  */

const argv = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(argv).pipe(fs.createWriteStream(file));
