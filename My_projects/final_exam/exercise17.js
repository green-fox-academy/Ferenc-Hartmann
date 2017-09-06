'use strict'

// Create a function that takes an array and a number and shifts the values of the array by the given number like: [1, 2, 3, 4, 5] and 2 becomes [4, 5, 1, 2, 3]

const mrSmith = [1, 2, 3, 4, 5];
const number = 2;


const funFunFunction = function (mrSmith, number) {
  let neoList = [];
  let counter = 0;
  for (let i = number; i > 0; i--) {
    neoList[counter] = mrSmith[mrSmith.length - i];
    counter++;
  }
  for (let i = 0; i < (mrSmith.length - number); i++) {
    neoList[counter] = mrSmith[i];
    counter++
  }
  return neoList;
}
console.log(funFunFunction(mrSmith, number));
