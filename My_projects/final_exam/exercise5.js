'use strict'

// Create a function that takes two arrays and decides if their content is the same

const firstArray = [1, 2, 3];
const secondArray = [1, 2, 3];

const funFunFunction = function (array1, array2) {
  let counter = 0;
  if (array1.length !== array2.length) {
    return 'not the same';
  }
  for (let i = 0; i < array1.length; i++) {
    if (array1[i] === array2[i]) {
      counter++;
    }
  }
  if (counter === array1.length) {
    return '100% same arrays';
  }
  else {
    return 'not the same';
  }
}
console.log(funFunFunction(firstArray, secondArray));
