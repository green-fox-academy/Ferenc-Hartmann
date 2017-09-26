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
    let dataToWrite;
    let codedData = '';
    let inputData = '';
    let fullTable = [];
    let fileName = '';

    if (process.argv.length < 4) {
      console.log('Usage: node zipper.js [filename to decompress] [decompressed filename]');
      process.exit(1);
    }
    console.log('File decompression started...');
    fileName = process.argv[2];
    fileRead();

    function fileRead() {
      let startTimeStamp;
      let endTimeStamp;
      startTimeStamp = new Date();

      fs.readFile(fileName, 'utf-8', function(err, data) {
        if (err) throw err;
        let readedData = data;

        endTimeStamp = new Date();
        console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
        console.log(data);

        dataTransformer(readedData);
      });
    }

    function dataTransformer(readedData) {
      let codeSequence = '';
      for (let i = 0; i < readedData.length; i++) {
        codeSequence += readedData[i].charCodeAt(0).toString(2);
      }
      console.log(codeSequence);
    }

    function keyTableBuild(readedData) {
      let startTimeStamp;
      let endTimeStamp;
      let keyTable = [];
      let codeTable = [];
      let code = [];
      let binaryCode = 0;
      let replaceNumber;

      startTimeStamp = new Date();

      for (let i = 0; i < readedData.length; i++) {
        if (readedData[i] == 0) {
          inputData += '0000';
        }
        if (readedData[i] == 1) {
          inputData += '0001';
        }
        if (readedData[i] == 2) {
          inputData += '0010';
        }
        if (readedData[i] == 3) {
          inputData += '0011';
        }
        if (readedData[i] == 4) {
          inputData += '0100';
        }
        if (readedData[i] == 5) {
          inputData += '0101';
        }
        if (readedData[i] == 6) {
          inputData += '0110';
        }
        if (readedData[i] == 7) {
          inputData += '0111';
        }
        if (readedData[i] == 8) {
          inputData += '1000';
        }
        if (readedData[i] == 9) {
          inputData += '1001';
        }
        if (readedData[i] == 'a') {
          inputData += '1010';
        }
        if (readedData[i] == 'b') {
          inputData += '1011';
        }
        if (readedData[i] == 'c') {
          inputData += '1100';
        }
        if (readedData[i] == 'd') {
          inputData += '1101';
        }
        if (readedData[i] == 'e') {
          inputData += '1110';
        }
        if (readedData[i] == 'f') {
          inputData += '1111';
        }
      }
      console.log(inputData);

      keyTable = inputData.split('0000000000000000')[0];
      keyTable = keyTable.split('00000000');
      let stringReverser = str => Array.prototype.reduce.call(str, (result, c) => c + result, "");

      for (let i = 0; i < keyTable.length; i++) {
        keyTable[i] = stringReverser(keyTable[i]);
      }

      keyTable = keyTable.reverse();
      console.log('keyTable', keyTable);


      codedData = inputData.split('0000000000000000')[1];
      codedData = codedData.split('00');
      console.log('codedData', codedData);

      for (let i = 0; i < codedData.length; i++) {
        code[i] = stringReverser(codedData[i]);
      }

      code = code.reverse();
      console.log('code', code);


      for (let i = 0; i < keyTable.length; i++) {
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
        codeTable[i] = binaryCode.toString(2) + '00';
      }


      endTimeStamp = new Date();
      console.log('keyTableBuild function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');

      decoder(keyTable, codeTable, code);
    }

    function decoder(keyTable, codeTable, code) {
      let i = code.length;
      let codeMinusOne = code.length - 1;
      let startTimeStamp;
      let endTimeStamp;
      let oneCycleData;
      let decodedData = '';
      startTimeStamp = new Date();

      while(i--) {
        let j = keyTable.length;
        oneCycleData = code[codeMinusOne - i];
        while(j--) {
          if (oneCycleData === codeTable[j]) {
            decodedData += keyTable[j];
            break;
          }
        }
      }


      endTimeStamp = new Date();
      console.log('decoder function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
      fileWrite(decodedData);

    }

    function fileWrite(decodedData) {
      let startTimeStamp;
      let endTimeStamp;
      let compressedFileName = process.argv[3];
      startTimeStamp = new Date();

      let dataToWrite = decodedData;
      let dataInTypedArray = Uint8Array.from(dataToWrite);
      fs.writeFile(compressedFileName, Buffer.from(dataInTypedArray.buffer), 'utf-8', function(err) {
        if (err) {
          return console.error(err);
        }
        endTimeStamp = new Date();
        console.log('fileWrite function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
        console.log(process.argv[2] + ' file decompressed successfully into ' + process.argv[3]);
      });
    }
  }
  return {
      init: init
  }
})();


MultiThreadProcess.init();




//     function binaryCoder(inputData) {
//       let codeSequence = '';
//       let workerData = [];
//       let fullTableMinusOne = fullTable.length - 1;
//       let threads = require('os').cpus().length;
//       let fullTableZero = [];
//       let fullTableOne = [];
//       let fullTableLength = fullTable.length;
//       let inputDataLength = inputData.length;
//       console.log('Compression algorithm started on ' + threads + ' CPU cores.');
//
//       for (let i = 0; i < fullTableLength; i++) {
//         fullTableZero[i] = fullTable[i][0];
//         fullTableOne[i] = fullTable[i][1];
//       }
//
//       function workSlicer() {
//         let dividedTable = Math.floor(inputDataLength / threads);
//
//         for (let i = 0; i < threads; i++) {
//           if (i !== (threads - 1)) {
//             slicedInputData[i] = inputData.slice((i * dividedTable), ((i + 1) * dividedTable));
//           } else {
//             slicedInputData[i] = inputData.slice((i * dividedTable));
//           }
//         }
//       };
//       workSlicer()
//
//       // Receive messages from worker and handle them in the master process.
//       cluster.on('message', function(worker, msg) {
//         codedArray[worker.id - 1] = msg.tempCodedData;
//       });
//
//       // If any worker dies this process starts.
//       cluster.on('exit', function(worker, msg) {
//
//         if (Object.keys(cluster.workers).length == 0) {
//           codedData = codedArray.join('');
//           MultiThreadProcess.singleThreadFunction(cluster, fs, codedData, fullTable);
//         }
//       });
//
//       for (let i = 0; i < threads; i++) {
//           let worker = cluster.fork();
//
//           // Send a message from the master process to the worker.
//           worker.send({fullTableOne: fullTableOne, fullTableZero: fullTableZero, slicedInputData: slicedInputData[worker.id - 1]});
//       }
//     }
//
//   }
//
//   function workerProcess(cluster) {
//     process.on('message', function(msg) {
//       let startTimeStamp;
//       let endTimeStamp;
//       let i = msg.slicedInputData.length;
//       let tempCodedData = '';
//       let oneCycleData;
//       let slicedInputDataMinusOne = msg.slicedInputData.length - 1;
//
//       for (let k = 0; k < msg.fullTableZero.length; k++) {
//         msg.fullTableZero[k] =  String.fromCharCode(msg.fullTableZero[k]);
//       }
//
//       startTimeStamp = new Date();
//
//       function encoder(j) {
//         if (oneCycleData === msg.fullTableZero[j]) {
//           tempCodedData += msg.fullTableOne[j];
//         }
//       }
//
//       while(i--) {
//         let j = msg.fullTableOne.length;
//         oneCycleData = msg.slicedInputData[slicedInputDataMinusOne - i];
//         break
//         while(j--) {
//           encoder(j)
//         }
//       }
//       // console.log(cluster.worker.id + '   ' + msg.zeroArray)
//       endTimeStamp = new Date();
//       console.log('binaryCoder function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
//
//       // Send message to master process.
//       process.send({tempCodedData: tempCodedData})
//       cluster.worker.kill();
//     });
//
//   }
//
//   function singleThreadFunction(cluster, fs, codedData, fullTable) {
//     cluster.setupMaster()
//     if (cluster.isMaster) {
//       function fileWrite(codedData) {
//         let startTimeStamp;
//         let endTimeStamp;
//         let fileName = process.argv[2].split(".")[0] + '.zap';
//         let codeSequence = '';
//         startTimeStamp = new Date();
//         for (let i = 0; i < fullTable.length; i++) {
//           codeSequence += fullTable[i][0].toString(2);
//         }
//         codeSequence += '000000000000000000000000';
//         let dataToWrite = codeSequence + codedData;
//         let dataInTypedArray = Uint8Array.from(dataToWrite);
//         let buffer = new ArrayBuffer(Math.ceil(dataToWrite.length/8));
//         for (let i = 0; i < dataToWrite.length; i++) {
//           buffer[i] = dataToWrite[i];
//         }
//         fs.writeFile(fileName, new Buffer(buffer), function(err) {
//           if (err) {
//             return console.error(err);
//           }
//           endTimeStamp = new Date();
//           console.log('fileWrite function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
//           console.log(process.argv[2] + ' file compressed successfully into ' + fileName);
//         });
//       }
//       fileWrite(codedData);
//     }
//   }
//
//   return {
//       init: init,
//       singleThreadFunction: singleThreadFunction
//   }
//
// })();
//
//
// MultiThreadProcess.init();
