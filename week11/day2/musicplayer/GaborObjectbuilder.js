'use strict'

const Ajax = function() {
    this.get = function(render) {
        // Get request -> respond
        let respond = 'respond';
        console.log(respond);
        render(respond);
    }
}

const Controller = function() {
    this.ajax = new Ajax();
    this.x = 'this is x';
    
    this.init = function() {
        this.ajax.get(this.render.bind(this));
    }
    this.render = function(respond) {
        console.log(this.x);
    }
}

const controller = new Controller();
controller.init();
