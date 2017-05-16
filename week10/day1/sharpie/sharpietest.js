'use strict'

var test = require('tape');

var sharpie = require('./sharpie');

test('Initalizing variables', function (t) {
    var product = new sharpie('green', 30);
	t.equals( product.color, 'green');
	t.equals( product.width, 30);
    t.equals( product.inkAmount, 100);
    t.equals( typeof product.use, 'function');
    t.end();
});

test('inside function test', function (t) {
    var product = new sharpie('green', 30);
    t.equals( product.inkAmount, 100);
    product.use();
    t.equals( product.inkAmount, 70);
    t.end();
});

test('only string input test', function (t) {
    var product = new sharpie('green', 'green');
    t.equals( product.color, 'green');
	t.equals( product.width, 'green');
    t.end();
});

test('only integer input test', function (t) {
    var product = new sharpie(50, 75);
    t.equals( product.color, 50);
	t.equals( product.width, 75);
    t.end();
});

test('no input', function (t) {
    var product = new sharpie();
    t.equals( product.color, 0);
	t.equals( product.width, 0);
    t.end();
});
