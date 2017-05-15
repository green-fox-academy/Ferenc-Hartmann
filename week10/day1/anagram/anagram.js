'use strict'

var anagramCheck = function(str1, str2) {
    return str1.split('').sort().join().toLowerCase() ===
     str2.split('').sort().join().toLowerCase() ? true : false;
};

module.exports = anagramCheck;
