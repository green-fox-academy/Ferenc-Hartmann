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


app.listen(8080);
