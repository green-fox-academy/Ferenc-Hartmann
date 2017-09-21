'use strict'
const fs = require('fs');

function fileRead() {
  let startTimeStamp;
  let endTimeStamp;
  let fileName = 'alma.zap';
  let inputData = '';
  startTimeStamp = new Date();

  fs.readFile(fileName, 'utf-8', function(err, data) {
    if (err) throw err;
    for (let i = 0; i < data.length; i++) {
      inputData = data;
    }
    endTimeStamp = new Date();
    console.log('fileRead function duration: ' + (endTimeStamp.getTime() - startTimeStamp.getTime()) + ' msec');
    console.log(data);
  });
}
fileRead()
