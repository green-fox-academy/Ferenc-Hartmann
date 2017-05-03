'use strict';
// Reverse the string!

var reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI";
var reverselist = [];

for (var i = (reversed.length-1); i >= 0 ; i--) {
    reverselist.push(reversed[i]);
}
reverselist = (reverselist.join(''));
console.log(reverselist);
