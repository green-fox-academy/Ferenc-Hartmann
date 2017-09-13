var cluster = require('cluster');
var numCPUs = require('os').cpus().length;

console.log('ezt neee');
console.log(cluster);
if (cluster.isMaster) {
  for (var i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  cluster.on('exit', function(worker, code, signal) {
    console.log("worker " + worker.id + " died");
    if (Object.keys(cluster.workers).length == 0) {
      console.log('Csak egy maradt');
      alma();
    }
  });
} else if (cluster.isWorker) {
  cluster.worker.kill();
  console.log(cluster.worker.id + 'WORKER WORKS');
}

function alma() {
  cluster.setupMaster()
  console.log("egyke");
  if (cluster.isMaster) {
    console.log("master ");
  }
}


// var cluster = require('cluster');
// var numCPUs = require('os').cpus().length;
// if (cluster.isMaster) {
//   for (var i = 0; i < numCPUs; i++) {
//     cluster.fork();
//   }
//   cluster.on('exit', function(worker, code, signal) {
//     console.log("worker " + worker.id + " died");
//     if (worker.id == numCPUs) {
//       alma();
//     }
//   });
// } else if (cluster.isWorker) {
//   cluster.worker.kill();
//   console.log(cluster.worker.id);
//
// } else if (cluster.isMaster) {
//   console.log("master ");
// }
//
// function alma() {
//   cluster.setupMaster()
//   console.log("egyke");
//   if (cluster.isMaster) {
//     console.log("master ");
//   }
// }
