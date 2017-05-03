'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(number) {
    var summer = 0;
    for (var i = 0; i < (number); i++) {
        summer += i;
    }
    return summer;
}
console.log(sum(5));
