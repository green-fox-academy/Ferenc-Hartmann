'use strict'

// Create a function takes a string and a letter and splits the string to an list of strings by the letter like: "a,bcd,e,fg" and ',' becomes ["a", "bcd", "e", "fg"]

const string = 'a,bcd,e,fg';
const letter = ',';

const funFunFunction = function (string, letter) {
  let neoList = [];
  let littleString = '';
  let counter = 0;

  for (let i = 0; i < (string.length); i++) {
    if (string[i] !== letter) {
      littleString += string[i];
    }
    else {
      neoList[counter] = littleString;
      littleString = '';
      counter++;
    }
  }
  if (littleString !== '') {
    neoList[counter] = littleString;
  }
  return neoList;
}
console.log(funFunFunction(string, letter));
