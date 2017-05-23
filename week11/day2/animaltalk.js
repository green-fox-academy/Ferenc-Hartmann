'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

var Animals = function(said) {
    this.sayer = said;
};

Animals.prototype.say = function() {
    console.log(this.sayer);
};


var macska = new Animals('miau');
macska.say();
