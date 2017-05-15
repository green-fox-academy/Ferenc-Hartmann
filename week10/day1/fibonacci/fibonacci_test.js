'use strict'

var test = require('tape');

var fibo = require('./fibonacci');

test('basic 5 test', function (t) {
    t.equal(fibo(5), 3);
    t.end();
});

test('0 test', function (t) {
    t.equal(fibo(0), 0);
    t.end();
});

test('1 test', function (t) {
    t.equal(fibo(1), 1);
    t.end();
});

test('negative test', function (t) {
    t.equal(fibo(-5), 'Fibonacci sequence starts from zero');
    t.end();
});
