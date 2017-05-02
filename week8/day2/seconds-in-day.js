'use strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

var Hoursleft = 24 - currentHours;
var Minutesleft = 60 - currentMinutes;
var Secondsleft = 60 - currentSeconds;
var seconds = Secondsleft + Minutesleft * 60 + Hoursleft * 60 * 60;

console.log(seconds);
