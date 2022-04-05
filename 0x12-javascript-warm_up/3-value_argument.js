#!/usr/bin/node

const argv = process.argv;

if (!argv[2]) {
  console.log('No argument');
} else {
  for (let i = 2; argv[i] != null; i++) {
    console.log(argv[i]);
  }
}
