'use strict'

var test = require('tape');

var newSharpie = require('./sharpie');

test('basic function test', function (t) {
    t.deepEquals(newSharpie('green', 30), { color: 'green', width: 30, inkAmount: 100, use: [Function] });
    t.end();
});

test('basic function test', function (t) {
    t.equal(newSharpie('green', 30).use, 70);
    t.end();
});
