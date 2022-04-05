#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
