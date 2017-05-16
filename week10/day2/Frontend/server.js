'use strict'
//localhost:8080
var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.use('/assets', express.static('assets'));
app.use(bodyParser.json());

app.get ('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get ('/doubling', function(req, res) {
    if (req.query.input === undefined) {
        var output = '';
        output = {
            error: "Please provide an input!"
        };
        res.send(output);
    } else {
        var delta = '';
        delta = {
            received: (1 * req.query.input),
            result: (2 * req.query.input)
        };
        res.send(delta);
    };
});

app.get ('/greeter', function(req, res) {
    if (req.query.name === undefined) {
        var output = '';
        output = {
            error: 'Please provide a name!'
        };
        res.send(output);
    }
    if (req.query.title === undefined) {
        var output = '';
        output = {
            error: 'Please provide a title!'
        };
        res.send(output);
    } else {
        var delta = '';
        delta = {
            welcome_message: 'Oh, hi there ' + req.query.name + ', my dear ' + req.query.title + '!'
        };
        res.send(delta);
    };
});

app.get ('/appenda/:id', function(req, res) {
    if (req.params.id === undefined) {
        req.params.id = bikicsunaj;
    }
    else {
        res.send(
            {
          appended: req.params.id + 'a',
        });
    }
});

app.post ('/dountil/:id', function(req, res) {
    if (req.params.id === 'sum') {
        var output = req.body.until;
        var sum = 0;
        for (var i = 1; i < (output + 1); i++) {
            sum = sum + i;
        }
        res.send(
            {
          result: sum
        });
    }
    else {
        var output = req.body.until;
        var factorial = 1;
        for (var i = 1; i < (output + 1); i++) {
            factorial = factorial * i;
        }
        res.send(
            {
          result: factorial
        });
    }
});

app.post ('/arrays', function(req, res) {
    if (req.body.what === undefined || typeof req.body.what === 'number') {
        res.send(
            {
         error: 'Please provide what to do with the numbers!'
        });
    }
    if (req.body.what === 'sum') {
        var respond = req.body.numbers.reduce((a, b) => a + b, 0);
        res.send(
            {
        result: respond
        });
    }
    if (req.body.what === 'multiply') {
        var respond = req.body.numbers.reduce((a, b) => a * b, 1);
        res.send(
            {
        result: respond
        });
    }
    if (req.body.what === 'double') {
        var respond = req.body.numbers.map(x => x * 2);
        res.send(
            {
        result: respond
        });
    }
});


app.listen(8080);
