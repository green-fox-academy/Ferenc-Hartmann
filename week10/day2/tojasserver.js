'use strict'
//localhost:3000
var express = require('express');

var app = express();

app.get ('/', function(req, res) {
    console.log(req.query);
    res.send({
        name: 'Balozska',
        age: '12',
        gender: 'male',
        banon: req.query.banon
    });
});

app.get ('/five', function(req, res) {
    res.send('five in klingon language: vagh');
});

app.listen(3000);
