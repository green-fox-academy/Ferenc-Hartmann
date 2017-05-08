'use strict'
var test = require('tape');

var arraytest = [0,0,0,4,5,6,7,8,9];
// [9,0,0,4,5,6,7,8,9] => Should fail
// [1,2,3,4,5,6,7,8,9] => ok
// [2,1,3,4,5,6,7,8,9] => ok
// [9,8,7,6,5,1,2,4,9] => Should fail
// [9,8,7,6,5,1,2,4,'u'] => Shold fail (non integer)
// [1,2,4,5] => NOPE
function validate(array) {
    if (array === undefined) {
        return false;
    }
    var lengthCheck = array.length;
    if (lengthCheck === 9) {
        var typecheck = 0;
        for (var i = 0; i < (array.length); i++) {
            if (typeof array[i] === 'number') {
                typecheck++;
            }
        }
        if (typecheck === 9) {
            for (var digit = 1; digit < 9; digit++) {
                var multiCheck = 0;
                for (var element = 0; element < array.length; element++) {
                    if (digit === array[element]) {
                        multiCheck ++;
                        if (multiCheck > 1) {
                            return false;
                        }
                    }
                }
            }
            element = 0;
            for (element = 0; element < (array.length); element++) {
                if (array[element] < 0) {
                    return false;
                }
            }
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    };
}

test('validate test', function (t) {
    t.equal(validate(),false);
    t.end();
})

test('length check', function (t) {
    t.equal(validate([13]),false);
    t.equal(validate([0,0,0,0,0,0,0,0,0]),true);
    t.equal(validate([1,1,1,1,1,5,5,1,1,1,1]), false);
    t.end();
})

test('similarity check', function (t) {
    t.equal(validate([1,1,1,1,'r',1,1,1,1]), false);
    t.end();
})

test('multi check', function (t) {
    t.equal(validate([0,0,0,1,4,1,7,8,9]), false);
    t.end();
})

test('negative check', function (t) {
    t.equal(validate([0,0,0,1,-4,5,7,8,9]), false);
    t.end();
})
