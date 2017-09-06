'use strict'

// Create a function that takes a number returns a matrix (list of lists) with height and width as the number, all of it's elments should be zero, beside the main diagonal should be ones like:
//
// 1 0 0 0 0
// 0 1 0 0 0
// 0 0 1 0 0
// 0 0 0 1 0
// 0 0 0 0 1

const number = '5';

const funFunFunction = function (number) {
  let matrix = [];
  for (let i = 0; i < number; i++) {
    matrix[i] = [];
    for (let j = 0; j < number; j++) {
      matrix[i][j] = 0;
      matrix[i][i] = 1;
    }
  }
  return matrix;
}
console.log(funFunFunction(number));
