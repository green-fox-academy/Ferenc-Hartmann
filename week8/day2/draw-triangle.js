'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

var star = '*';

for (var i = 0; i < 4; i++) {
  console.log(star);
  star += '*';
}
