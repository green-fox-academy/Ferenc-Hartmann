'use strict'

// Create a function that takes a list of strings and a letter and returns a string where the strings are joined with the given letter like: ["ab", "cde", "fg"] and " " becomes "ab cde fg"

const list = ['ab', 'cde', 'fg'];
const letter = ' ';

const funFunFunction = function (list, letter) {
  let littleString = '';

  for (let i = 0; i < (list.length); i++) {
    littleString += (list[i] + letter);
  }
  return littleString;
}
console.log(funFunFunction(list, letter));
