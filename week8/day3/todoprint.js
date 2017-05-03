'use strict';
// Add "My todo:" to the beginning of the todoText
// Add " - Download games" to the end of the todoText
// Add " - Diablo" to the end of the todoText but with indention

// Expected outpt:

// My todo:
//  - Buy milk
//  - Download games
//      - Diablo

var todoText = " - Buy milk\n";


var todoText = todoText.replace(/ - Buy milk\n/, 'My todo:\n - Buy milk\n');
var todoText = todoText.replace(/ - Buy milk\n/, ' - Buy milk\n - Download games\n');
var todoText = todoText.replace(/ - Download games\n/, ' - Download games\n     - Diablo');

console.log(todoText);
