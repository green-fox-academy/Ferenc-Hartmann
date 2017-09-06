'use strict'

// Create a function that takes a string and a letter, than returns a list that contains all the indexes where the letter occured in the string.


const string = 'malomipar';
const letter = 'm';

const funFunFunction = function (string, letter) {
  let positions = [];
  let counter = 0;
  for (let i = 0; i < (string.length - 1); i++) {
    if (string[i] === letter) {
      positions[counter] = i;
      counter++;
    }
  }
  return positions;
}
console.log(funFunFunction(string, letter));
