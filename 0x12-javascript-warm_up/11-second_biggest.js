#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 2) {
  console.log('0');
} else {
  let num = 0;
  let tmp = 0;
  for (let i = 2; argv[i] != null; i++) {
    if (num < argv[i]) {
      tmp = num;
      num = argv[i];
    } else if (tmp < argv[i]) {
      tmp = argv[i];
    }
  }
  console.log(tmp);
}
