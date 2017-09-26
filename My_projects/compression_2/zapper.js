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

    if (process.argv.length < 3) {
      console.log('Usage: node zapper.js [filename to compress] [compressed filename]');
      process.exit(1);
    }
    console.log('File compression started...');
    fileRead();

    function fileRead() {
      let startTimeStamp;
      let endTimeStamp;
      let fileName = process.argv[2];
      let inputData;
      startTimeStamp = new Date();

      fs.readFile(fileName, 'hex', function(err, data) {
        if (err) throw err;
        inputData = data;

        endTimeStamp = new Date();
        console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
        inputDataSlicer(inputData);
      });
    }


    function inputDataSlicer(inputData) {
      let startTimeStamp;
      let endTimeStamp;
      let inputDataInArray = [];
      let i = 0;
      startTimeStamp = new Date();

      for (i; i < inputData.length - 4; i++) {
        if ((i % 4) == 0) {
          inputDataInArray.push(inputData.slice(i, i + 4));
        }
      }
      if (i == (inputData.length - 4) && (i % 4) == 0) {
        inputDataInArray.push(inputData.slice(i, - 1));
      } else {
        inputDataInArray.push(inputData.slice(-(i % 4), inputData.length));
      }

      endTimeStamp = new Date();
      console.log('inputDataSlicer function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      probabilityTableInitializer(inputDataInArray);
    }

    function probabilityTableInitializer(inputDataInArray) {
      let startTimeStamp;
      let endTimeStamp;
      let probabilityBasicTable = [];
      let oneKey = [];
      startTimeStamp = new Date();

      for (let i = 0; i < inputDataInArray.length; i++) {
        oneKey = [inputDataInArray[i], 1];
        probabilityBasicTable.push(oneKey);
      }

      probabilityBasicTable.sort();

      endTimeStamp = new Date();
      console.log('probabilityTableInitializer function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      probabilityCalculator(inputDataInArray, probabilityBasicTable);
    }

    function probabilityCalculator(inputDataInArray, probabilityBasicTable) {
      let startTimeStamp;
      let endTimeStamp;
      let probabilityTable = [];
      let onePair = probabilityBasicTable[0];
      startTimeStamp = new Date();

      for (let i = 0; i < probabilityBasicTable.length - 1; i++) {
        if (onePair[0] == probabilityBasicTable[i + 1][0]) {
          onePair[1] += 1;
          if ((i + 1) == (probabilityBasicTable.length - 1)) {
            probabilityTable.push(onePair);
          }
        }
        else {
          probabilityTable.push(onePair);
          onePair = probabilityBasicTable[i + 1];
          if ((i + 1) == (probabilityBasicTable.length - 1)) {
            probabilityTable.push(onePair);
          }
        }
      }
      endTimeStamp = new Date();
      console.log('probabilityCalculator function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      probabilityTableSorter(inputDataInArray, probabilityTable);
    }

    function probabilityTableSorter(inputDataInArray, probabilityTable) {
      let startTimeStamp;
      let endTimeStamp;
      startTimeStamp = new Date();

      function Comparator(a, b) {
        if (a[1] < b[1]) return 1;
        if (a[1] > b[1]) return -1;
        return 0;
      }

      probabilityTable.sort(Comparator);

      endTimeStamp = new Date();
      console.log('probabilityTableSorter function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      staticKeyTableGenerator(inputDataInArray, probabilityTable);
    }

    function staticKeyTableGenerator(inputDataInArray, probabilityTable) {
      let startTimeStamp;
      let endTimeStamp;
      let oneCodePair = [];
      let staticKeyTable = [];
      startTimeStamp = new Date();

      for (let number = 0; number < 65536; number++) {
        let oneCodePair = [];
        oneCodePair.push(number.toString(16));
        oneCodePair.push(number.toString(15) + 'f');
        staticKeyTable.push(oneCodePair);
        if (number == 65535) {
          dynamicKeyTableGenerator(inputDataInArray, probabilityTable, staticKeyTable);
        }
      }
    }

    function dynamicKeyTableGenerator(inputDataInArray, probabilityTable, staticKeyTable) {
      let startTimeStamp;
      let endTimeStamp;
      let dynamicKeyTable = probabilityTable;
      startTimeStamp = new Date();
      for (let i = 0; i < probabilityTable.length; i++) {
        dynamicKeyTable[i][1] = staticKeyTable[i][1];
      }

      endTimeStamp = new Date();
      console.log('dynamicKeyTableGenerator function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      // dynamicKeyTableGenerator(inputDataInArray, probabilityTable, staticKeyTable);
    }

// eddig jó! :)
// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



    function characterCalc(inputData) {
      let startTimeStamp;
      let endTimeStamp;
      startTimeStamp = new Date();

      endTimeStamp = new Date();
      console.log('characterCalc function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');

      codeTableBuilder(inputData);
    }

    function binaryCoder(inputData) {
      console.log('Compression algorithm started on ' + threads + ' CPU cores.');

      // Receive messages from worker and handle them in the master process.
      cluster.on('message', function(worker, msg) {
      });

      // If any worker dies this process starts.
      cluster.on('exit', function(worker, msg) {

        if (Object.keys(cluster.workers).length == 0) {
          MultiThreadProcess.singleThreadFunction(cluster, fs);
        }
      });

      for (let i = 0; i < threads; i++) {
          let worker = cluster.fork();

          // Send a message from the master process to the worker.
          worker.send({});
      }
    }
  }

  function workerProcess(cluster) {
    process.on('message', function(msg) {
      startTimeStamp = new Date();

      endTimeStamp = new Date();
      console.log('binaryCoder function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');

      // Send message to master process.
      process.send({})
      cluster.worker.kill();
    });

  }

  function singleThreadFunction(cluster, fs) {
    cluster.setupMaster()
    if (cluster.isMaster) {
      function fileWrite() {
        let startTimeStamp;
        let endTimeStamp;
        startTimeStamp = new Date();

        fs.writeFile( process.argv[3], data, 'hex', function(err) {
          if (err) {
            return console.error(err);
          }
          endTimeStamp = new Date();
          console.log('fileWrite function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
          console.log(process.argv[2] + ' file compressed successfully into ' + process.argv[3]);
        });
      }
      fileWrite(codedData);
    }
  }

  return {
      init: init,
      singleThreadFunction: singleThreadFunction
  }

})();


MultiThreadProcess.init();
