'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
    var factorial = 1;
    for (var i = 1; i < (number + 1); i++) {
        factorial = factorial * i;
    }
    return factorial;
}
console.log(factorio(5));
