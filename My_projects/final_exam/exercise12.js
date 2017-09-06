'use strict'

// Create a function that takes a matrix (list of lists) of numbers and returns the sum of each rows as an array

const mrSmith = [
  [1, 2, 3],
  [4, 5, 6],
  [2, 4, 6]];

const funFunFunction = function (matrix) {
  let array = [];
  let sum = 0;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      sum += matrix[i][j];
    }
    array[i] = sum;
    sum = 0;
  }
  return array;
}
console.log(funFunFunction(mrSmith));
