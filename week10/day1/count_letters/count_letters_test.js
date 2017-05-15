'use strict'

var test = require('tape');

var letterCounter = require('./count_letters');

test('basic alma test', function (t) {
    t.deepEquals(letterCounter('alma'), { a: 2, l: 1, m: 1 });
    t.end();
});

test('numbers in string test', function (t) {
    t.deepEquals(letterCounter('alma111'), { a: 2, l: 1, m: 1 });
    t.end();
});

test('numbers in string test2', function (t) {
    t.deepEquals(letterCounter('11alma111'), { a: 2, l: 1, m: 1 });
    t.end();
});

test('uppercase test', function (t) {
    t.deepEquals(letterCounter('11aLMA111'), { a: 2, l: 1, m: 1 });
    t.end();
});
