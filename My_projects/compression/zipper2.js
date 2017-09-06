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

    fs.readFile(fileName, 'utf8', function(err, data) {
      if (err) throw err;
      inputData = data;

      characterCalc(inputData, fileName);
    });
  }

  function characterCalc(inputData, fileName) {
    let keyTable = [];
    let oneKey = [];
    let fullTable = [];

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
  }

  function codeTableBuilder(fullTable, fileName, inputData) {
    while (fullTable.length > 2) {
      let oneHuffmanPair = fullTable.slice(-2);
      fullTable = fullTable.slice(0, -2)
      let oneHuffmanConc = [];
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
      oneHuffmanConc.push((oneHuffmanPair[0][0] + oneHuffmanPair[1][0]));
      oneHuffmanConc.push((oneHuffmanPair[0][1] + oneHuffmanPair[1][1]));
      oneHuffmanConc.push(simpleArray);
      while ((fullTable.length + counter) !== 0 && oneHuffmanConc[1] > fullTable[fullTable.length + counter][1]) {
        counter--;
      }
      fullTable.splice((fullTable.length + counter + 1), 0, oneHuffmanConc);

    }
    let oneHuffmanConc = [];
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
    oneHuffmanConc.push((fullTable[0][0] + fullTable[1][0]));
    oneHuffmanConc.push((fullTable[0][1] + fullTable[1][1]));
    oneHuffmanConc.push(simpleArray);
    fullTable = oneHuffmanConc;

    let binaryKeyTable = [];
    for (let i = 0; i < fullTable[0].length; i++) {
      binaryKeyTable.push([fullTable[0][i], fullTable[2][i]]);
    }
    console.log(binaryKeyTable);

    BinaryCoder(binaryKeyTable, fileName, inputData);
  }

  function BinaryCoder(fullTable, fileName, inputData) {
    let codedData = '';
    let codeSequence = '';

    for (let i = 0; i < inputData.length; i++) {
      for (let j = 0; j < fullTable.length; j++) {
        if (inputData[i] == fullTable[j][0]) {
          codedData += fullTable[j][1];
        }
      }
    }

    for (let i = 0; i < fullTable.length; i++) {
      codeSequence += fullTable[i][0].codePointAt().toString(2);
    }
    codeSequence += '00000000';

    let dataForUtf = codeSequence + codedData;
    utfCoder(dataForUtf, fileName);
  }

  function utfCoder(dataForUtf, fileName) {
    let fullyCoded = '';

    let hangya = [];
    for (let i = 0; i < 128; i++) {
      let code = String.fromCharCode(i);
      hangya.push(code);
    }

    for (let i = 1; i <= (dataForUtf.length / 7); i++) {
      let slicedData = dataForUtf.slice(7 * (i -1), (7 * i));
      let slicedDecimalData = parseInt(slicedData, 2);
      fullyCoded += hangya[slicedDecimalData];
    }

    fileWrite(fullyCoded, fileName)
  }

  function fileWrite(fullyCoded, name) {
    let fileName = name.split(".")[0] + '.zap';

    fs.writeFile(fileName, fullyCoded, function(err) {
      if (err) {
        return console.error(err);
      }
      console.log(name + ' file compressed successfully into ' + fileName);
    });
  }

  return {
      init: init
  }

})();

FileIO.init();
