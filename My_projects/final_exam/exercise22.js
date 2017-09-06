'use strict'

// Create a function that takes an array of integers and returns a new one consisting only those numbers that occured minimum twice in the original array

const mrSmith = [1, 3, 9, 4, 6, 3, 7, 6, 8, 6, 2, 2];

const funFunFunction = function (mrSmith, neo) {
  let neoList = [];
  let counter = 0;
  let counter2 = 0;
  let counter3 = 0;

  for (let i = 0; i < mrSmith.length; i++) {
    for (let j = 0; j < mrSmith.length; j++) {
      if (mrSmith[i] === mrSmith[j]) {
        counter++;
      }
    }
    if (counter > 1) {
      for (let k = 0; k < neoList.length; k++) {
        if (mrSmith[i] === neoList[k]) {
          counter3++;
        }
      }
      if (counter3 === 0) {
        neoList[counter2] = mrSmith[i];
        counter2++;
      }
      counter3 = 0;
    }
    counter = 0;
  }
  return neoList;
}
console.log(funFunFunction(mrSmith));
