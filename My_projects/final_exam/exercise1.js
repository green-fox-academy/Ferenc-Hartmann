'use strict'

// Create a function that takes a matrix (list of lists) of numbers and sums all the numbers.

const mrSmith = [
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3]];

const funFunFunction = function (matrix) {
  let sum = 0;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      sum += matrix[i][j];
    }
  }
  return sum;
}
console.log(funFunFunction(mrSmith));
