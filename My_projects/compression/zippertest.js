'use strict'

const MultiThreadProcess = (function() {

  function init() {
    const cluster = require('cluster');
    const fs = require('fs');

    if (cluster.isMaster) {
      masterProcess(cluster, fs);
    } else if (cluster.isWorker) {
      workerProcess(cluster);
    }
  }

  function masterProcess(cluster, fs) {
    const threads = require('os').cpus().length;
    let exampleArray = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]];
    let finishedArray = [];

    if (process.argv.length < 3) {
      console.log('Usage: node zipper.js [filename]');
      process.exit(1);
    }
    console.log('File compression started...');
    fileRead();

    function fileRead() {
      let startTimeStamp;
      let endTimeStamp;
      let inputData;
      let fileName = process.argv[2];
      let name = fileName.split('.')[0];
      startTimeStamp = new Date();

      fs.readFile(fileName, 'utf8', function(err, data) {
        if (err) throw err;
        inputData = data;

        endTimeStamp = new Date();
        console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
        characterCalc(inputData, fileName);
      });
    }

    function characterCalc(inputData, fileName) {
      let startTimeStamp;
      let endTimeStamp;
      let keyTable = [];
      let oneKey = [];
      let fullTable = [];
      startTimeStamp = new Date();

      for (let i = 0; i < inputData.length; i++) {
        oneKey = [inputData[i], 1];
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
      endTimeStamp = new Date();
      console.log('characterCalc function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      codeTableBuilder(fullTable, fileName, inputData);
    }

    function codeTableBuilder(fullTable, fileName, inputData) {
      let startTimeStamp;
      let endTimeStamp;
      let binaryCode = 0;
      let replaceNumber;
      startTimeStamp = new Date();

      for (let i = 0; i < fullTable.length; i++) {
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
        fullTable[i][1] = binaryCode.toString(2) + '00';
      }
      endTimeStamp = new Date();
      console.log('codeTableBuilder function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      // binaryCoder(fullTable, fileName, inputData);
    }



    cluster.on('exit', function(worker) {
      finishedArray[worker.id - 1] = exampleArray[worker.id - 1][0] + exampleArray[worker.id - 1][1];
      if (Object.keys(cluster.workers).length == 0) {
        MultiThreadProcess.singleThreadFunction(cluster, finishedArray);
      }
    });

    for (let i = 0; i < threads; i++) {
        cluster.fork();
    }
  }

  function workerProcess(cluster) {
    cluster.worker.kill();
  }

  function singleThreadFunction(cluster, finishedArray) {
    cluster.setupMaster()
    if (cluster.isMaster) {
      console.log(finishedArray);
    }
  }

  return {
      init: init,
      singleThreadFunction: singleThreadFunction
  }

})();


MultiThreadProcess.init();
