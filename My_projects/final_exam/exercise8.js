'use strict'

// Create a function that takes two arrays and mixes them like this: [1, 2, 3] and [6, 7, 8] becomes [1, 6, 2, 7, 3, 8]

const mrSmith = [1, 2, 3];
const neo = [6, 7, 8];

const funFunFunction = function (mrSmith, neo) {
  let total = [];
  let counter = 0;
  if (mrSmith.length !== neo.length) {
    console.log('arrays are not the same in length');
  }
  for (let i = 0; i < mrSmith.length; i++) {
    total[counter] = mrSmith[i];
    total[counter + 1] = neo[i];
    counter +=2;
  }
  return total;
}
console.log(funFunFunction(mrSmith, neo));
