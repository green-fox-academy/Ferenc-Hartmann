'use strict'

var test = require('tape');

var sum = require('./sum');

test('sum test', function (t) {
    t.equal(sum([0, 1, 2, 3]), 6);
    t.end();
});

test('zero list test', function (t) {
    t.equal(sum([]), 0);
    t.end();
});

test('one element in test', function (t) {
    t.equal(sum([6]), 6);
    t.end();
});

test('sum test not ordered list', function (t) {
    t.equal(sum([3, 1, 2]), 6);
    t.end();
});

test('sum test for null', function (t) {
    t.equal(sum([null]), 0);
    t.end();
});

test('sum test for null and numbers', function (t) {
    t.equal(sum([1, null, 2]), 3);
    t.end();
});

test('sum test for null and numbers', function (t) {
    t.equal(sum([1, 'string', 2]), 3);
    t.end();
});
