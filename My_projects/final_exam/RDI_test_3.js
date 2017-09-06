// 3.	Write a method that can determine if a given integer number is odd or even. It is ONLY allowed to use addition or subtraction operations (do NOT use modulus ‘%’, shift ‘<<’, multiply, divide, etc.). Return true if even.
// bool IsEven(int number)


'use strict'

const funFunFunction = function (integer) {
  let number = integer;
  let i = 0;
  while (number > 0) {
    number -= 2;
    i += 1;
  }
  if (number == 0) {
    return true;
  }
  if (number == -1) {
    return false;
  }
}
console.log(funFunFunction(18));
