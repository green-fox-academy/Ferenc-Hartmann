'use strict';
// - Create a variable named `ai` with the following content: `[3, 4, 5, 6, 7]`
// - Log the sum of the elements in `ai` to the console

var ai = [3, 4, 5, 6, 7];
var sum = 0

ai.forEach(function(i) {
    sum += i;
});

console.log(sum);
