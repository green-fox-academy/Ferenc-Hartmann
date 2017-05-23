'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

var Rectangles = function(aSide, bSide) {
    this.aSide = aSide;
    this.bSide = bSide;
};

Rectangles.prototype.getArea = function() {
    return this.aSide * this.bSide;
};

Rectangles.prototype.getCircumference = function() {
    return 2 * this.aSide + 2 * this.bSide;
};

var rect = new Rectangles(10, 20);
console.log(rect.getArea());
console.log(rect.getCircumference());
