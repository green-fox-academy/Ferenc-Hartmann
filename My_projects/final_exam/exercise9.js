'use strict'

// Create a function that takes an array of integers and retunrs the biggest from each of its second elements like: [1, 3, 8, 6, 7, 4] would return 6

const mrSmith = [1, 3, 8, 6, 7, 6];

const funFunFunction = function (mrSmith) {
  let biggest = 0;
  for (let i = 1; i < mrSmith.length; i += 2) {
    if (mrSmith[i] > biggest) {
      biggest = mrSmith[i];
    }
  }
  return biggest;
}
console.log(funFunFunction(mrSmith));
