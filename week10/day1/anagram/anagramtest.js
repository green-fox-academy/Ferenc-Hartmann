'use strict'

var test = require('tape');

var anagramCheck = require('./anagram');

test('basic true test', function (t) {
    t.equal(anagramCheck('alma', 'mala'), true);
    t.end();
});

test('basic false test', function (t) {
    t.equal(anagramCheck('alma', 'malc'), false);
    t.end();
});

test('length test', function (t) {
    t.equal(anagramCheck('alma', 'mal'), false);
    t.end();
});
