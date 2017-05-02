'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

var star = '*'
var space = ' '
var j = 1;
var k = 0;

for (var i = 0; i < lineCount; i++) {
    if (i < (lineCount + 1) / 2) {
        console.log(space.repeat((lineCount-(i + (lineCount / 2)))) + star + space.repeat((lineCount-(i + (lineCount / 2)))));
        star += '**';
    } else {
        star = '*';
        k = lineCount - 2 * j;
        console.log(space.repeat(j) + star.repeat(k) + space.repeat(j));
        j = j + 1;
    }
}
