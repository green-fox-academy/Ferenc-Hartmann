'use strict'
//localhost:3000
var http = require('http');

var server = http.createServer(handleRequest);

function handleRequest(request, response) {
    console.log(request);
    response.end('Hello');
}
server.listen(3000);
