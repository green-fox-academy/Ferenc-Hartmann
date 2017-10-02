'use strict'

const fs = require('fs');

fs.readFile('almi.txt', 'hex', function(err, data) {
  if (err) throw err;
  console.log(data);
});

console.log(Number('65533').toString(15))
