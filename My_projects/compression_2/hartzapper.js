'use strict'

const Compressor = (function() {

  function init() {
    const cluster = require('cluster');
    const fs = require('fs');

    cluster.isMaster ? masterProcess(cluster, fs) : workerProcess(cluster);
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
        if (a[1] < b[1]) return 1;
        if (a[1] > b[1]) return -1;
        return 0;
      }

      probabilityTable.sort(Comparator);

      const endTimeStamp = new Date();
      console.log('probabilityTableSorter function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      hartmannFunction(inputDataInArray, probabilityTable);
    }

    function hartmannFunction(inputDataInArray, probabilityTable) {
      hartmannCodeTable = [];
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
          Compressor.singleThreadFunction(cluster, fs, codedData, hartmannCodeTable);
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
      const slicedInputDataMinusOne = msg.slicedInputDataInArray.length - 1;
      const msghartmannCodeTableZero = msg.hartmannCodeTableZero;
      const msghartmannCodeTableOne = msg.hartmannCodeTableOne;

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
      let dataToWrite = '';

      hartmannCodeTable.forEach(e => e[1] = parseInt(e[1], 2).toString(16));

      if (codedData.length % 4 !== 0) {
        let alma = codedData.length - (codedData.length % 4);
        console.log('last chars: ', codedData.substring((codedData.length - (codedData.length % 4)), codedData.length))
        dataToWrite += codedData.substring((codedData.length - (codedData.length % 4)), codedData.length)
        codedData = codedData.slice(0, (codedData.length - (codedData.length % 4)));
      }

      dataToWrite += 'fff';

      for (let i = 0; i < hartmannCodeTable.length; i++) {
        dataToWrite += hartmannCodeTable[i][0].toString(15);
        dataToWrite += 'f';
      }
      dataToWrite += 'fff';



      for (var i = 0; i < codedData.length - 4; i++) {
        if ((i % 4) == 0) {
          dataToWrite += parseInt(codedData.slice(i, i + 4), 2).toString(16);
        }
      }
      if (i == (codedData.length - 4) && (i % 4) == 0) {
        dataToWrite += parseInt(codedData.slice(i, codedData.length), 2).toString(16);
      }

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


// -------------------------------------------------------------------------------------
// DECOMPRESSION STARTS HERE


const Decompressor = (function() {

  function init() {
    const cluster = require('cluster');
    const fs = require('fs');

    cluster.isMaster ? masterProcess(cluster, fs) : workerProcess(cluster);
  }

  function masterProcess(cluster, fs) {
    const threads = require('os').cpus().length;
    let hartmannCodeTable = [];
    let codedData;
    let codedDataSupport;
    let codedArray = [];

    if (process.argv.length < 3) {
      console.log('Usage: node zapper.js [filename to decompress] [decompressed filename]');
      process.exit(1);
    }
    console.log('File decompression started...');
    fileRead();

    function fileRead() {
      const fileName = process.argv[2];
      const startTimeStamp = new Date();

      fs.readFile(fileName, 'hex', function(err, data) {
        if (err) throw err;
        codedDataSupport = data.slice(0, data.indexOf('fff'));
        const codedKeytable = data.slice((data.indexOf('fff') + 3), data.indexOf('ffff'));
        codedData = data.slice((data.indexOf('ffff') + 4), data.length);
console.log(codedKeytable)

        const endTimeStamp = new Date();
        console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
        keyTableDecoder(codedKeytable);
      });
    }

    function keyTableDecoder(codedKeytable) {
      let decodedKeytable = [];
      const startTimeStamp = new Date();

      decodedKeytable = Array.from(codedKeytable.split('f'), x => parseInt(x, 15).toString(16));

      const endTimeStamp = new Date();
      console.log('keyTableDecoder function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      keyTableValueGenerator(decodedKeytable);
    }

    function keyTableValueGenerator(decodedKeytable) {
      let binaryCode = 0;
      let replaceNumber;
      const startTimeStamp = new Date();

      decodedKeytable.forEach(e => hartmannCodeTable.push([(e), ['']]));

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
        hartmannCodeTable[i][1] = binaryCode.toString(2);
      }
      const endTimeStamp = new Date();
      console.log('keyTableValueGenerator function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      codedDataToBinary();
    }

    function codedDataToBinary() {
      let binaryCodedData = '';
      const startTimeStamp = new Date();

      for (let i = 0; i < codedData.length; i++) {
        if (codedData[i] == 0) {
          binaryCodedData += '0000';
        }
        if (codedData[i] == 1) {
          binaryCodedData += '0001';
        }
        if (codedData[i] == 2) {
          binaryCodedData += '0010';
        }
        if (codedData[i] == 3) {
          binaryCodedData += '0011';
        }
        if (codedData[i] == 4) {
          binaryCodedData += '0100';
        }
        if (codedData[i] == 5) {
          binaryCodedData += '0101';
        }
        if (codedData[i] == 6) {
          binaryCodedData += '0110';
        }
        if (codedData[i] == 7) {
          binaryCodedData += '0111';
        }
        if (codedData[i] == 8) {
          binaryCodedData += '1000';
        }
        if (codedData[i] == 9) {
          binaryCodedData += '1001';
        }
        if (codedData[i] == 'a') {
          binaryCodedData += '1010';
        }
        if (codedData[i] == 'b') {
          binaryCodedData += '1011';
        }
        if (codedData[i] == 'c') {
          binaryCodedData += '1100';
        }
        if (codedData[i] == 'd') {
          binaryCodedData += '1101';
        }
        if (codedData[i] == 'e') {
          binaryCodedData += '1110';
        }
        if (codedData[i] == 'f') {
          binaryCodedData += '1111';
        }
      }

      const endTimeStamp = new Date();
      console.log('codedDataToBinary function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      dataToArray(binaryCodedData);
    }

    function dataToArray(binaryCodedData) {
      let inputDataInArray = [];
      const startTimeStamp = new Date();

      binaryCodedData = ('00' + binaryCodedData + codedDataSupport);

      inputDataInArray = binaryCodedData.substring(0, (binaryCodedData.length - 2)).split('001');
      inputDataInArray.splice(0, 1);

      for (let i = 0; i < inputDataInArray.length; i++) {
        inputDataInArray[i] = ('1' + inputDataInArray[i]);
      }

      const endTimeStamp = new Date();
      console.log('dataToArray function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
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
console.log('hartmannCodeTable')
console.log(hartmannCodeTable)
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
          Decompressor.singleThreadFunction(cluster, fs, codedData, hartmannCodeTable);
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
      const slicedInputDataMinusOne = msg.slicedInputDataInArray.length - 1;
      let msghartmannCodeTableZero = msg.hartmannCodeTableZero;
      const msghartmannCodeTableOne = msg.hartmannCodeTableOne;

      const startTimeStamp = new Date();

      while(i--) {
        let j = msg.hartmannCodeTableOne.length;
        oneCycleData = msg.slicedInputDataInArray[slicedInputDataMinusOne - i];
        while(j--) {
          if (oneCycleData === msghartmannCodeTableOne[j]) {
            tempCodedData += msghartmannCodeTableZero[j];
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
      fileWriter(codedData);
    }

    function fileWriter(codedData) {
      const startTimeStamp = new Date();
      fs.writeFile( process.argv[3], codedData, 'hex', function(err) {
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

// App starts here:
process.argv[2].includes('.zap') ? Decompressor.init() : Compressor.init();
