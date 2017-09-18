'use strict'

const MultiThreadProcess = (function() {

  function init() {

    const cluster = require('cluster');
    const fs = require('fs');

    if (cluster.isMaster) {
      const threads = require('os').cpus().length;
      let exampleArray = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]];
      let finishedArray = [];
      for (let i = 0; i < threads; i++) {
        let worker = cluster.fork();

        // Send a message from the master process to the worker.
        worker.send({oneArray: exampleArray[worker.id -1], alma: 'alma'});
      }

      // If any worker dies this process starts.
      cluster.on('exit', function(worker) {
        if (Object.keys(cluster.workers).length == 0) {
          MultiThreadProcess.singleThreadFunction(cluster, finishedArray);
        }
      });

      // Receive messages from cluster and handle them in the master process.
      cluster.on('message', function(worker, msg) {
        finishedArray[worker.id -1] = msg.oneNumber;
      });

    } else if (cluster.isWorker) {
      process.on('message', function(msg) {
        let oneNumber = msg.oneArray[0] + msg.oneArray[1];
        console.log(msg.alma);
        process.send({oneNumber: oneNumber})
      });
      cluster.worker.kill();
    }

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
