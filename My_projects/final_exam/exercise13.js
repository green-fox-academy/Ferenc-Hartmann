'use strict'

// Create a function that takes a list of strings and transforms it like:
//
// [
//   "abc",
//   "ijk",
//   "xyz"
// ]
// becomes
//
// [
//   "aix",
//   "bjy",
//   "ckz"
// ]

const mrSmith = [
  "abc",
  "ijk",
  "xyz"
]

const funFunFunction = function (stringList) {
  let array = [];
  for (let i = 0; i < stringList.length; i++) {
    array[i] = '';
    for (let j = 0; j < stringList[i].length; j++) {
      array[i] += stringList[j][i];
    }
  }
  return array;
}

console.log(funFunFunction(mrSmith));
