'use strict';

// Adds a and b, returns as result
const addNumbers = function(a, b) {
    return typeof a ==='number' && typeof b ==='number' ? a + b : 'invalid value';
}

// Returns the highest value from the three given params
const maxOfThree = function(a, b, c) {
    if (typeof a ==='number' && typeof b ==='number' && typeof c === 'number') {
        if ((a > b) && (a > c)) {
            return a;
        } else if ((b > a) && (b > c)) {
            return b;
        } else {
            return c;
        }
    }
    else {
        return 'Invalid value';
    }
}

//Returns the median value of a list given as param
const median = function(pool){
    let ret = 0;
    pool.forEach(function(element){
        if (typeof element === 'string') {
            ret = 'Invalid value';
        }
    });
    if (ret === 0) {
        ret = (pool.filter((x) => typeof x === 'number')).reduce((a, b) => a + b, 0) / pool.length;
        return ret;
    }
    else {
        return ret;
    }
}

// Returns true if the param is a vovel
const isVovel = function(char){
    if (char === '') {
        return 'Please, give me one character';
    }
    else if (char.length > 1) {
        return 'Please, give me one character';
    }

    else {
        return 'aeiouéáőűöüóí'.indexOf(char) >= 0 ? true : false;
    }
}

// Create a method that translates hungarian into the teve language
const translate = function(hungarian) {
    if (typeof hungarian === 'number') {
        return 'Invalid value';
    }
    else {
        let text = String(hungarian).toLowerCase().split('');
        let teve = '';
        text.forEach(function(char){
            if (isVovel(char) === false){
            teve += char;
            }
            else if (isVovel(char)){
              teve += char + 'v'+ char;
            }
        });
        return teve;
    }
}

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}
