'use strict'

var anagramCheck = function(str1, str2) {
    let str1Converted = str1.split('').sort().join().toLowerCase();
    let str2Converted = str2.split('').sort().join().toLowerCase();
    return str1Converted === str2Converted ? true : false;
};

module.exports = anagramCheck;
