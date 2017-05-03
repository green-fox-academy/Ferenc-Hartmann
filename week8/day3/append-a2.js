'use strict';
// - Create a variable named `nimals`
//   with the following content: `["kuty", "macs", "cic"]`
// - Add all elements an `"a"` at the end
// - try to use built in functions instead of loops

var nimals = ["kuty", "macs", "cic"];

var alphabet = nimals.map(function(num) {
  return num + 'a';
});

nimals = alphabet
console.log(nimals);
