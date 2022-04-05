#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  return num1 + num2;
}
console.log(add(argv[2], argv[3]));
