'use strict'

var letterCounter = function(string) {
    let counter = 1;
    let lettersNumbers = {};
    let convertedString = string.toLowerCase().split('').sort();
    for (let i = 0; i < (convertedString.length); i++) {
        if (convertedString[i] % 1 == 0) {
            counter = 0;
        }
        if (convertedString[i] !== convertedString[i+1] && (convertedString[i] % 1 !== 0)) {
            lettersNumbers[convertedString[i]] = counter;
            counter = 1;
        }
        else {
            counter +=1;
        }
    }
    return lettersNumbers;
};

module.exports = letterCounter;
console.log(letterCounter('11alma111'))
