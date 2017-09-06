'use strict'

// Create a function that takes two strings and returns an array of characters that consitst all the common letters of the two arrays

const string1 = 'alma';
const string2 = 'macska';

const funFunFunction = function (string1, string2) {
  let letters = '';
  let counter = 0;

  for (let i = 0; i < string1.length; i++) {
    for (let k = 0; k < letters.length; k++) {
      if (letters[k] == string1[i] || letters[k] == string2[i]) {
        counter++;
      }
    }
    if (counter === 0) {
      letters += string1[i];
    }
    counter = 0;
  }
    return letters
}
console.log(funFunFunction(string1, string2));
