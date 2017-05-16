'use strict'

var test = require('tape');

var animal = require('./animal');

test('Initalizing variables', function (t) {
    var product = new animal();
	t.equals( product.hunger, 50);
	t.equals( product.thirst, 50);
    t.equals( typeof product.eat, 'function');
    t.equals( typeof product.drink, 'function');
    t.equals( typeof product.play, 'function');
    t.end();
});
