'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs:
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function candies() {
    var a = [];
    var candies = 0;
    for (var i = 0; i < (students.length); i++) {
        for (var j = 0; j < (arguments.length); j++) {
            arguments[j] === students[i]['name'] ? a.push(students[i]['candies']) : '';
        }
    }
    for (var k = 0; k < (arguments.length); k++) {
        candies = candies + a[k];
    }
    console.log(candies);
    }


function ageSum() {
    var a = [];
    var age = 0;
    for (var i = 0; i < (students.length); i++) {
        for (var j = 0; j < (arguments.length); j++) {
            arguments[j] === students[i]['name'] && students[i]['candies'] < 5 ? a.push(students[i]['age']) : '';
        }
    }
    for (var k = 0; k < (arguments.length); k++) {
        typeof a[k] === 'number' ? age = age + a[k] : '';
    }
    console.log(age);
    }


candies('Teodor', 'Rezso', 'Olaf')
ageSum('Teodor', 'Rezso', 'Olaf')
