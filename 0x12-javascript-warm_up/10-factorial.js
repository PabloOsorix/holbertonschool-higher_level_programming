#!/usr/bin/node

const argv = process.argv;

function factorial (a) {
  const num = parseInt(a);
  let factorial = 1;

  if (isNaN(num)) {
    return factorial;
  } else {
    for (let i = 1; i <= num; i++) {
      factorial *= i;
    }
    return factorial;
  }
}
console.log(factorial(argv[2]));
