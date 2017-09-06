'use strict'

// Create a function that reverses a string

const string = 'malomipar';

const funFunFunction = function (string) {
  let reverse = '';
  for (let i = (string.length - 1); i >= 0; i--) {
    reverse += string[i];
  }
  return reverse;
}
console.log(funFunFunction(string));
