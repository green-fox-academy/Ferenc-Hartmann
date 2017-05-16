'use strict'
//localhost:8080
var express = require('express');

var app = express();
app.use('/assets', express.static('assets'));

app.get ('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

// app.get ('/doubling/input=:id', function(req, res) {
//     res.send(
//         {
//       "received": req.params.id,
//       "result": 2 * req.params.id
//     });
// });

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


app.listen(8080);
