'use strict'

// Create a function that takes a string and splits it to a list of two character strings like: "abcdef" becomes ["ab", "cd", "ef"]

const string = 'abcdef';

const funFunFunction = function (string) {
  let neoList = [];
  let littleString = '';
  let counter = 0;

  for (let i = 0; i < (string.length); i++) {
    littleString += string[i];
    if (i % 2 === 1) {
      neoList[counter] = littleString;
      littleString = '';
      counter++;
    }
  }
  return neoList;
}
console.log(funFunFunction(string));
