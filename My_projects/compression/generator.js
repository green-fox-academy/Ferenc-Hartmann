'use strict'

const fs = require('fs');

let binaryCode = 0;
let replaceNumber;
let hartmannTable = [];
let binaryTable = [];
let codeTable = [];
let oneCodePair = [];
let i = 0;

for (i; i < 65536; i++) {
  let oneCodePair = [];
  let counter = 0;
  while (binaryCode.toString(2).indexOf('00') > 0) {
    replaceNumber = binaryCode.toString(2).replace('00', '01');
    binaryCode = parseInt(replaceNumber, 2);
    counter++;
  }

  if (counter == 0) {
    binaryCode++;
    while (binaryCode.toString(2).indexOf('00') > 0) {
      replaceNumber = binaryCode.toString(2).replace('00', '01');
      binaryCode = parseInt(replaceNumber, 2);
    }
  }
  oneCodePair.push(i.toString(2));
  oneCodePair.push(binaryCode.toString(2) + '00');
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
