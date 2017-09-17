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
          cluster.fork();
      }

      cluster.on('exit', function(worker) {
        finishedArray[worker.id - 1] = exampleArray[worker.id - 1][0] + exampleArray[worker.id - 1][1];
        if (Object.keys(cluster.workers).length == 0) {
          MultiThreadProcess.singleThreadFunction(cluster, finishedArray);
        }
      });

    } else if (cluster.isWorker) {
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
