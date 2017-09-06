'use strict'

// Create a function that takes a list of numbers and returns a new list where all the duplicate values are removed

const list = [1, 2, 3, 2, 1, 5];

const funFunFunction = function (list) {
  let neoList = [];
  let counter1 = 0;
  let counter2 = 0;

  for (let i = 0; i < list.length; i++) {
    for (let j = 0; j < list.length; j++) {
      if (list[i] === list[j]) {
        counter1++;
      }
    }
    if (counter1 === 1) {
      neoList[counter2] = list[i];
      counter2++;
    }
    counter1 = 0;
  }
    return neoList
}
console.log(funFunFunction(list));
