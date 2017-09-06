'use strict'

// Create a function that takes two list of numbers and returns a new list that only consists those numbers that are in the first array but not in the second

const mrSmith = [1, 3, 9, 4, 6, 7, 6, 8, 2];
const neo = [1, 3, 9, 6, 7, 6, 8, 11];

const funFunFunction = function (mrSmith, neo) {
  let neoList = [];
  let counter = 0;
  let counter2 = 0;

  for (let i = 0; i < mrSmith.length; i++) {
    for (let j = 0; j < neo.length; j++) {
      if (mrSmith[i] === neo[j]) {
        counter++;
      }
    }
    if (counter === 0) {
      neoList[counter2] = mrSmith[i];
      counter2++;
    }
    counter = 0;
  }
  return neoList;
}
console.log(funFunFunction(mrSmith, neo));
