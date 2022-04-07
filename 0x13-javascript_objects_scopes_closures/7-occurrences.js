#!/usr/bin/node
/*  Function that retuurns number of occurrences
in a list   */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; list[i] != null; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
