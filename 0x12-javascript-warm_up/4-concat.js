#!/usr/bin/node

const argv = process.argv;

if (!argv[2] && !argv[3]) {
  console.log('undefined is undefined');
} else {
  console.log(argv[2] + ' is ' + argv[3]);
}
