'use strict'

const fs = require('fs');

const FileIO = (function() {

  function init() {
    if (process.argv.length < 3) {
      console.log('Usage: node zipper.js [filename]');
      process.exit(1);
    }
    fileRead();
  }

  function fileRead() {
    let inputData;
    let fileName = process.argv[2];
    let name = fileName.split('.')[0];
    let startTimeStamp1;
    let endTimeStamp1;
    startTimeStamp1 = new Date();

    fs.readFile(fileName, 'utf8', function(err, data) {
      if (err) throw err;
      inputData = data;

      characterCalc(inputData, fileName);
    });
    endTimeStamp1 = new Date();
    console.log('fileRead duration: ' + (endTimeStamp1.getTime() - startTimeStamp1.getTime()) + 'msec');
  }

  function characterCalc(inputData, fileName) {
    let keyTable = [];
    let oneKey = [];
    let fullTable = [];
    let startTimeStamp2;
    let endTimeStamp2;
    startTimeStamp2 = new Date();

    for (let i = 0; i < inputData.length; i++) {
      oneKey = [inputData[i], 1, []];
      keyTable.push(oneKey);
    }

    keyTable.sort();
    let oneKey2 = keyTable[0];
    for (let j = 0; j < keyTable.length - 1; j++) {
      if (oneKey2[0] == keyTable[j + 1][0]) {
        oneKey2[1] += 1;
        if ((j + 1) == (keyTable.length - 1)) {
          fullTable.push(oneKey2);
        }
      }
      else {
        fullTable.push(oneKey2);
        oneKey2 = keyTable[j + 1];
        if ((j + 1) == (keyTable.length - 1)) {
          fullTable.push(oneKey2);
        }
      }
    }

    function Comparator(a, b) {
      if (a[1] < b[1]) return 1;
      if (a[1] > b[1]) return -1;
      return 0;
    }

    fullTable.sort(Comparator);
    codeTableBuilder(fullTable, fileName, inputData);
    endTimeStamp2 = new Date();
    console.log('characterCalc duration: ' + (endTimeStamp2.getTime() - startTimeStamp2.getTime()) + 'msec');
  }

  function codeTableBuilder(fullTable, fileName, inputData) {
    let startTimeStamp3;
    let endTimeStamp3;
    startTimeStamp3 = new Date();
    while (fullTable.length > 2) {
      let oneHuffmanPair = fullTable.slice(-2);
      fullTable = fullTable.slice(0, -2)
      let oneHuffmanNode = [];
      let simpleArray = [];
      let counter = -1;

      if (oneHuffmanPair[0][2][0] == undefined) {
        oneHuffmanPair[0][2].push('0');
      } else {
        for (let i = 0; i < oneHuffmanPair[0][2].length; i++) {
          oneHuffmanPair[0][2][i] = '0' + oneHuffmanPair[0][2][i];
        }
      }

      if (oneHuffmanPair[1][2][0] == undefined) {
        oneHuffmanPair[1][2].push('1');
      } else {
        for (let i = 0; i < oneHuffmanPair[1][2].length; i++) {
          oneHuffmanPair[1][2][i] = '1' + oneHuffmanPair[1][2][i];
        }
      }

      for (let i = 0; i < oneHuffmanPair[0][2].length; i++) {
        simpleArray.push(oneHuffmanPair[0][2][i]);
      }
      for (let i = 0; i < oneHuffmanPair[1][2].length; i++) {
        simpleArray.push(oneHuffmanPair[1][2][i]);
      }

      oneHuffmanNode.push((oneHuffmanPair[0][0] + oneHuffmanPair[1][0]));
      oneHuffmanNode.push((oneHuffmanPair[0][1] + oneHuffmanPair[1][1]));
      oneHuffmanNode.push(simpleArray);
      while ((fullTable.length + counter) !== 0 && oneHuffmanNode[1] > fullTable[fullTable.length + counter][1]) {
        counter--;
      }
      fullTable.splice((fullTable.length + counter + 1), 0, oneHuffmanNode);

    }

    let oneHuffmanNode = [];
    let simpleArray = [];
    let counter = -1;
    if (fullTable[0][2][0] == undefined) {
      fullTable[0][2].push('0');
    } else {
      for (let i = 0; i < fullTable[0][2].length; i++) {
        fullTable[0][2][i] = '0' + fullTable[0][2][i];
      }
    }
    if (fullTable[1][2][0] == undefined) {
      fullTable[1][2].push('1');
    } else {
      for (let i = 0; i < fullTable[1][2].length; i++) {
        fullTable[1][2][i] = '1' + fullTable[1][2][i];
      }
    }
    for (let i = 0; i < fullTable[0][2].length; i++) {
      simpleArray.push(fullTable[0][2][i]);
    }
    for (let i = 0; i < fullTable[1][2].length; i++) {
      simpleArray.push(fullTable[1][2][i]);
    }
    oneHuffmanNode.push((fullTable[0][0] + fullTable[1][0]));
    oneHuffmanNode.push((fullTable[0][1] + fullTable[1][1]));
    oneHuffmanNode.push(simpleArray);
    fullTable = oneHuffmanNode;

    let binaryKeyTable = [];
    for (let i = 0; i < fullTable[0].length; i++) {
      binaryKeyTable.push([fullTable[0][i], fullTable[2][i]]);
    }

    binaryCoder(binaryKeyTable, fileName, inputData);
    endTimeStamp3 = new Date();
    console.log('codeTableBuilder duration: ' + (endTimeStamp3.getTime() - startTimeStamp3.getTime()) + 'msec');
  }

  function binaryCoder(fullTable, fileName, inputData) {
    let codedData = '';
    let codeSequence = '';
    let startTimeStamp4;
    let endTimeStamp4;
    startTimeStamp4 = new Date();

    for (let i = 0; i < inputData.length; i++) {
      for (let j = 0; j < fullTable.length; j++) {
        if (inputData[i] == fullTable[j][0]) {
          codedData += fullTable[j][1];
        }
      }
    }

    fullTable = fullTable.toString();

    for (let i = 0; i < fullTable.length; i++) {
        codeSequence += fullTable[i].codePointAt().toString(2);
    }
    codeSequence += '0000000000000000000000000000000000000000';
    let dataToWrite = codeSequence + codedData;

    fileWrite(dataToWrite, fileName);
    endTimeStamp4 = new Date();
    console.log('binaryCoder duration: ' + (endTimeStamp4.getTime() - startTimeStamp4.getTime()) + 'msec');
  }

  function fileWrite(dataToWrite, name) {
    let fileName = name.split(".")[0] + '.zap';
    let dataInTypedArray = Uint8Array.from(dataToWrite);
    let startTimeStamp5;
    let endTimeStamp5;
    startTimeStamp5 = new Date();

    let buffer = new ArrayBuffer(Math.ceil(dataToWrite.length/8));
    for (let i = 0; i < dataToWrite.length; i++) {
      buffer[i] = dataToWrite[i];
    }
    fs.writeFile(fileName, new Buffer(buffer), function(err) {
      if (err) {
        return console.error(err);
      }
      endTimeStamp5 = new Date();
      console.log('fileWrite duration: ' + (endTimeStamp5.getTime() - startTimeStamp5.getTime()) + 'msec');
      console.log(name + ' file compressed successfully into ' + fileName);
    });
  }

  return {
      init: init
  }

})();

FileIO.init();






// 'use strict'
//
// const fs = require('fs');
//
// const str = '010101011010101001100111';
// const hangya = Uint8Array.from(str);
//
// let buffer = new ArrayBuffer(Math.ceil(str.length/8));
// for (let i = 0; i < str.length; i++) {
//   buffer[i] = str[i];
// }
// console.log(Math.ceil(str.length/8));
// fs.writeFileSync('test.bin', new Buffer(buffer));
