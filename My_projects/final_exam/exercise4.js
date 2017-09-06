'use strict'

// Create a function that returns how many letters in the word: "duck" (it is four)

const string = 'duck';

const funFunFunction = function (string) {
  let sum = 0;
  for (let i = 0; i < string.length; i++) {
    sum++
  }
    return sum;
}
console.log(funFunFunction(string));
