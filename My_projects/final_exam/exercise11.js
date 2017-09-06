'use strict'

// Create a function that takes two strings and decides if one is anagram of the other

const string1 = 'apap';
const string2 = 'aapp';

const funFunFunction = function (string1, string2) {
  let string1Reordered = string1[0];
  let string2Reordered = string2[0];
  let counter1 = 0;
  let counter2 = 0;
  let counter3 = 0;

  if (string1.length === string2.length) {
    for (let i = 0; i < string1.length; i++) {
      for (let j = 0; j < string2.length; j++) {
        if (string1[i] === string2[j]) {
          counter1++
        }
        if (string2[i] === string1[j]) {
          counter2++
        }
      }
      if (counter1 === counter2) {
        counter3++;
      }
    }
    if (counter3 == string1.length) {
      return '100% anagrams'
    }
    else {
      return '0% anamgrams'
    }
  }
  else {
    return '0% anamgrams'
  }
}
console.log(funFunFunction(string1, string2));
