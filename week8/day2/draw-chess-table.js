'use strict';

// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
//


var block = '%'
var space = ' '
var x = block + space
var y = space + block

for (var i = 0; i < (5); i++) {
    console.log(x.repeat(4));
    console.log(y.repeat(4));
}
