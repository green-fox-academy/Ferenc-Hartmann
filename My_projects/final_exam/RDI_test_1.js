// 1.	Write a method that displays the first 100 Fibonacci numbers separated with commas. Example: the first 10 elements of the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 …


'use strict'

const FibonacciCalculator = (function() {
  let fiboRow = '';

  const oneFibonacci = function(num) {
    if (num == 0) {
      return 0;
    }
    if (num == 1) {
      return 1;
    }
    else {
      return oneFibonacci(num - 1) + oneFibonacci(num - 2);
    }
  }

  const stringifier = function(number) {

  for( let i = 0; i < number; i += 1) {
    fiboRow += oneFibonacci(i) + ', ';
  }
  fiboRow = fiboRow.slice(0, -2);
  console.log(fiboRow);
  }

  return {
      stringifier: stringifier
  }

})();

FibonacciCalculator.stringifier(100);
