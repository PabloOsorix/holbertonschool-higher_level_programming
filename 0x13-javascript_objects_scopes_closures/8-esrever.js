#!/usr/bin/node
//  function that returns the reversed version of a list.
exports.esrever = function (list) {
  const newList = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
