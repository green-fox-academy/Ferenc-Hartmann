'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

var selectLastEvenNumber = function(array, funk) {
    let oddNumbers = array.filter((x) => x % 2 === 0);
    funk(oddNumbers[oddNumbers.length-1]);
}

function printNumber(num) {
  console.log(num);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
