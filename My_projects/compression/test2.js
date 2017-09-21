'use strict'
const fs = require('fs');

function fileRead() {
  let startTimeStamp;
  let endTimeStamp;
  let fileName = 'alma.zap';
  let inputData = '';
  startTimeStamp = new Date();

  fs.readFile(fileName, 'binary', function(err, data) {
    if (err) throw err;
    endTimeStamp = new Date();
    console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
    console.log(data.length);
  });
}
fileRead()
