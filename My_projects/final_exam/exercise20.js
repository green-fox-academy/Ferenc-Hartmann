'use strict'

// Create a function that takes a list of numbers and returns the second biggest element from it

const mrSmith = [1, 3, 9, 6, 7, 6, 8];

const funFunFunction = function (mrSmith) {
  let biggest = 0;
  let secondBiggest = 0;

  for (let i = 0; i < mrSmith.length; i++) {
    if (mrSmith[i] > biggest) {
      biggest = mrSmith[i];
    }
  }
  for (let i = 0; i < mrSmith.length; i++) {
    if (mrSmith[i] > secondBiggest && mrSmith[i] !== biggest) {
      secondBiggest = mrSmith[i];
    }
  }

  return secondBiggest;
}
console.log(funFunFunction(mrSmith));
