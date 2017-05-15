'use strict'

var sum = function(integers) {
    var summarize = 0;
    for (var i = 0; i < integers.length; i++) {
        if (typeof integers[i] === 'number') {
        summarize += integers[i];
        }
    }
    return summarize;
}

module.exports = sum;
