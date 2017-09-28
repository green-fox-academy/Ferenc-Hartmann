'use strict'
var a = [[ 'a', '1' ], [ 'bc', '2' ], [ 'd', '3' ], [ 'ef', '4' ]];

// console.log(a.indexOf(2));
// console.log(a.indexOf(6));

// for (let i = 0; i < a.length-1; i++) {
//     console.log(a.indexOf('2'));
//     console.log(a.indexOf('6'));
//     console.log(a[i].indexOf('2'));
//     console.log(a[i].indexOf('6'));
// }

// function isBigEnough(element, search) {
//   return element.indexOf(search) >= 0;
// }

a.map(function(x, i) {
  if (x[0].indexOf('a') >= 0) { console.log(x) };
});


// console.log(a.find(isBigEnough, 'c'));
