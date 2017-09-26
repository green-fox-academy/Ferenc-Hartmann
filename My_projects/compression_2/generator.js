'use strict'

function generator(number) {
  let startTimeStamp;
  let endTimeStamp;
  let hartmannHexNumber;
  let codeTable = [];
  startTimeStamp = new Date();

    while(number--) {
      let oneCodePair = [];
      oneCodePair.push(number.toString(16));
      oneCodePair.push(number.toString(15) + 'f');
      codeTable.push(oneCodePair);
      if (number == 0) {
        writer(codeTable, startTimeStamp, endTimeStamp);
      }
    }
}

function writer(codeTable, startTimeStamp, endTimeStamp) {
  codeTable.reverse();
  console.log('codeTable[0]: ', codeTable[0]);
  console.log('codeTable[10]: ', codeTable[10]);
  console.log('codeTable[100]: ', codeTable[100]);
  console.log('codeTable[1000]: ', codeTable[1000]);
  console.log('codeTable[1000]: ', codeTable[10000]);
  console.log('codeTable[65535]: ', codeTable[65535]);
  console.log('codeTable[1000000]: ', codeTable[1000000]);
  console.log('codeTable[10000000]: ', codeTable[10000000]);
  console.log('codeTable[16777215]: ', codeTable[16777215]);
  endTimeStamp = new Date();
  console.log('codeTable generated in: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
}
generator(16*16*16*16);
