'use strict'

var test = require('tape');

var getApple = require('./apple');

test('return test', function (t) {
    t.equal(getApple(),'apple');
    t.end();
});
