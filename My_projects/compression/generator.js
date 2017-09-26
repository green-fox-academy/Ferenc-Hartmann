'use strict'

const fs = require('fs');

let i = 0;
let hartmannHexNumber;
let codeTable = [];

for (i; i < 65536; i++) {
  let oneCodePair = [];
  let counter = 0;
  oneCodePair.push(i.toString(16));
  oneCodePair.push(i.toString(15) + 'f');
  codeTable.push(oneCodePair);
  if (i == 65535) {
    writer();
  }
}

function writer() {
  console.log(codeTable[1]);
  console.log(codeTable[10]);
  console.log(codeTable[100]);
  console.log(codeTable[1000]);
  console.log(codeTable[10000]);
  console.log(codeTable[65535]);
  codeTable.toString();
  fs.writeFile('table.txt', JSON.stringify(codeTable), function(err) {
    if (err) {
      return console.error(err);
    }
  });
}
