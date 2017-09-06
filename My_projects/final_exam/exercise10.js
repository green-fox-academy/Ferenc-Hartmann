'use strict'

// Create a function that takes an array of integers and returns the average of the even numbers from that array

const mrSmith = [2, 1, 6];

const funFunFunction = function (mrSmith) {
  let total = 0;
  let counter = 0;
  for (let i = 0; i < mrSmith.length; i += 1) {
    if ( mrSmith[i] % 2 == 0) {
      total += mrSmith[i];
      counter++;
    }
  }
  let average = total / counter;
  return average;
}
console.log(funFunFunction(mrSmith));
