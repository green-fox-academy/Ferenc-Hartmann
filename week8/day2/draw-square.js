'use strict';

var lineCount = 10;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var block = '%'
var space = ' '

console.log(block.repeat((lineCount-1)));
for (var i = 0; i < (lineCount - 2); i++) {
    console.log(block + space.repeat(lineCount - 3) + block);
}
console.log(block.repeat((lineCount-1)));
