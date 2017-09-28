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
    let hartmannCodeTable;
    let codedData = '';
    let codedArray = [];

    if (process.argv.length < 3) {
      console.log('Usage: node zapper.js [filename to compress] [compressed filename]');
      process.exit(1);
    }
    console.log('File compression started...');
    fileRead();

    function fileRead() {
      const fileName = process.argv[2];
      const startTimeStamp = new Date();

      fs.readFile(fileName, 'utf-8', function(err, data) {
        if (err) throw err;
        const splittedData = data.split("");
        const inputDataInArray = splittedData.map(function(x) {
          return x.codePointAt();
        });
        const endTimeStamp = new Date();
        console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
        probabilityTableInitializer(inputDataInArray);
      });
    }

    function probabilityTableInitializer(inputDataInArray) {
      let probabilityBasicTable = [];
      const startTimeStamp = new Date();

      inputDataInArray.forEach(e => probabilityBasicTable.push([e]));

      probabilityBasicTable.sort();

      probabilityBasicTable.forEach(e => e.push(1));
      const endTimeStamp = new Date();
      console.log('probabilityTableInitializer function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      probabilityCalculator(inputDataInArray, probabilityBasicTable);
    }

    function probabilityCalculator(inputDataInArray, probabilityBasicTable) {
      let onePair = probabilityBasicTable[0];
      const probabilityTable = [];
      const startTimeStamp = new Date();

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
      const endTimeStamp = new Date();
      console.log('probabilityCalculator function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      probabilityTableSorter(inputDataInArray, probabilityTable);
    }

    function probabilityTableSorter(inputDataInArray, probabilityTable) {
      const startTimeStamp = new Date();

      function Comparator(a, b) {
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
        return 0;
      }

      //reversed probabilityTable
      probabilityTable.sort(Comparator);

      const endTimeStamp = new Date();
      console.log('probabilityTableSorter function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      hartmannFunction(inputDataInArray, probabilityTable);
    }


    function hartmannFunction(inputDataInArray, probabilityTable) {
      hartmannCodeTable = [];
      let oneArrayPair = [];
      let oneCombinedArrayPair = [];
      let binaryCode = 0;
      let replaceNumber;
      const startTimeStamp = new Date();

      probabilityTable.forEach(e => hartmannCodeTable.push([(e[0]), ['']]));

      for (let i = 0; i < hartmannCodeTable.length; i++) {
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
        hartmannCodeTable[i][1] = binaryCode.toString(2) + '00';
      }

      const endTimeStamp = new Date();
      console.log('hartmannFunction function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      workSlicer(inputDataInArray);
    }

    function workSlicer(inputDataInArray) {
      let slicedInputDataInArray = [];
      const startTimeStamp = new Date();
      const dividedTable = Math.floor(inputDataInArray.length / threads);

      for (let i = 0; i < threads; i++) {
        if (i !== (threads - 1)) {
          slicedInputDataInArray[i] = inputDataInArray.splice(0, dividedTable);
        } else {
          slicedInputDataInArray[i] = inputDataInArray;
        }
      }

      const endTimeStamp = new Date();
      console.log('workSlicer function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      multiThreadInvoker(slicedInputDataInArray);
    }

    function multiThreadInvoker(slicedInputDataInArray) {
      let hartmannCodeTableZero = [];
      let hartmannCodeTableOne =[];

      console.log('Compression algorithm started on ' + threads + ' CPU cores.');
      hartmannCodeTable.forEach((e, i) => { hartmannCodeTableZero[i] = e[0]; hartmannCodeTableOne[i] = e[1] } );

      // Receive messages from worker and handle them in the master process.
      cluster.on('message', function(worker, msg) {
        codedArray[worker.id - 1] = msg.tempCodedData;
      });

      // If any worker dies this process starts.
      cluster.on('exit', function(worker, msg) {

        if (Object.keys(cluster.workers).length == 0) {
          codedData = codedArray.join('');
          MultiThreadProcess.singleThreadFunction(cluster, fs, codedData, hartmannCodeTable);
        }
      });

      for (let i = 0; i < threads; i++) {
          let worker = cluster.fork();

          // Send a message from the master process to the worker.
          worker.send({ slicedInputDataInArray: slicedInputDataInArray[worker.id - 1], hartmannCodeTableZero: hartmannCodeTableZero, hartmannCodeTableOne: hartmannCodeTableOne });
      }
    }
  }

  function workerProcess(cluster) {
    process.on('message', function(msg) {
      let i = msg.slicedInputDataInArray.length;
      let tempCodedData = '';
      let oneCycleData;
      let slicedInputDataMinusOne = msg.slicedInputDataInArray.length - 1;
      let msghartmannCodeTableZero = msg.hartmannCodeTableZero;
      let msghartmannCodeTableOne = msg.hartmannCodeTableOne;

      const startTimeStamp = new Date();

      while(i--) {
        let j = msg.hartmannCodeTableOne.length;
        oneCycleData = msg.slicedInputDataInArray[slicedInputDataMinusOne - i];
        while(j--) {
          if (oneCycleData === msghartmannCodeTableZero[j]) {
            tempCodedData += msghartmannCodeTableOne[j];
            break;
          }
        }
      }

      const endTimeStamp = new Date();
      console.log('workerProcess function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');

      // Send message to master process.
      process.send({tempCodedData: tempCodedData})
      cluster.worker.kill();
    });

  }

  function singleThreadFunction(cluster, fs, codedData, hartmannCodeTable) {
    cluster.setupMaster()
    if (cluster.isMaster) {
      fileDataConstructer();
    }

    function fileDataConstructer() {
      const startTimeStamp = new Date();
      let decodedhartmannCodeTable = [];
      let dataToWrite = '[';

      hartmannCodeTable.forEach(e => e[1] = parseInt(e[1], 2));

      for (let i = 0; i < hartmannCodeTable.length; i++) {
        dataToWrite += hartmannCodeTable[i][0];
      }

      dataToWrite += ']';
// DataToWrite = codedData!!!!!!
      dataToWrite='';
      let i = 0;
      for (i = 0; i < codedData.length - 4; i++) {
        if ((i % 4) == 0) {
          dataToWrite += parseInt(codedData.slice(i, i + 4), 2).toString(16);
        }
      }
      if (i == (codedData.length - 4) && (i % 4) == 0) {
        dataToWrite += parseInt(codedData.slice(i, -1), 2).toString(16);
      } else {
        // dataToWrite += String.fromCharCode(parseInt((codedData.slice(-(i % 4), codedData.length)), 2));
        dataToWrite += parseInt(codedData.slice(-(i % 4), codedData.length), 2).toString(16);
      }
      dataToWrite += 'f';
      const endTimeStamp = new Date();
      console.log('fileDataConstructer function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      fileWriter(dataToWrite);
    }
    function fileWriter(dataToWrite) {
      const startTimeStamp = new Date();

      fs.writeFile( process.argv[3], dataToWrite, 'hex', function(err) {
        if (err) {
          return console.error(err);
        }
      });

      const endTimeStamp = new Date();
      console.log('fileWriter function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      console.log(process.argv[2] + ' file compressed successfully into ' + process.argv[3]);
    }
  }

  return {
      init: init,
      singleThreadFunction: singleThreadFunction
  }

})();


MultiThreadProcess.init();
