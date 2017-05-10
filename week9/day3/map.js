
'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.


// var eCounter = function(list){
//     let elemcounter = 0;
//     for (let i = 0; i < list.length; i++) {
//         if (list[i] === 'e') {
//             elemcounter++;
//         }
//     }
//     return elemcounter
// }
//
// var eAdder = fruits.map(eCounter);
// console.log(eAdder);


var splitter = fruits.map((x) => x.split(''));

var eFilter = splitter.map((y) => y.filter((x) => x === 'e'));

var eCounter = eFilter.map((z) => z.length);
console.log(eCounter);
