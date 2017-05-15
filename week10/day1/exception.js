'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2) {
    if (typeof str1 !== 'string') {
        throw new Error('"str1" is not a string')
    }
    else if (typeof str2 !== 'string') {
        throw new Error('"str2" is not a string')
    }
    else {
        let newStr = str1 + str2;
        printStr(newStr);
    }
}

let printStr = function(str) {
  console.log(str);
}

try {
	addString('1234', '56789');
} catch (err) {
	console.log('catching error:');
	console.log(err.message);
}
