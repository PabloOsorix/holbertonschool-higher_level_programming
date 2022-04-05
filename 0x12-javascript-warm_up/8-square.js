#!/usr/bin/node

const argv = process.argv;
const size = parseInt(argv[2]);

if (!size) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= size; i++) {
    console.log('X'.repeat(size));
  }
}
