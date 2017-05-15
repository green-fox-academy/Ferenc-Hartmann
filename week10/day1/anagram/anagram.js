'use strict'

// var sum = function(integers) {
//     var summarize = 0;
//     for (var i = 0; i < integers.length; i++) {
//         if (typeof integers[i] === 'number') {
//         summarize += integers[i];
//         }
//     }
//     return summarize;
// }


var sum = function(integers) {
    if (typeof integers[i] === 'number') {
        return integers.reduce((a, b) => a + b, 0);
    }
}

module.exports = sum;
