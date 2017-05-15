'use strict'

var fibo = function(number) {
    var list = [0, 1];
    var n = 0;
    if (number === 0) {
        return 0;
    }
    else if (number === 1) {
        return 1;
    }
    else if (number < 0){
        return 'Fibonacci sequence starts from zero';
    }
    else {
        while (n < number - 2) {
            list.push((list[list.length - 2] + list[list.length - 1]));
            n++;
        }
        return list[list.length-1];
    }
}

module.exports = fibo;
