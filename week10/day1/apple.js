'use strict'
var test = require('tape');

function getApple() {
    return 'apple'
}

test('return test', function (t) {
    t.equal(getApple(),'apple');
    t.end();
})
