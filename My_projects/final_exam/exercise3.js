'use strict'

// Create a function that determines if a string is a palindrome

const string = 'malam';

const funFunFunction = function (string) {
  let reverse = '';
  for (let i = (string.length - 1); i >= 0; i--) {
    reverse += string[i];
  }
  if (string === reverse) {
    return 'palindrome';
  }
  else {
    return 'not a palindrome';
  }
}
console.log(funFunFunction(string));
