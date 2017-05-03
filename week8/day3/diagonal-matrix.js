'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array


function matrixer(a) {
    var matrix = [];
    for (var j = 0; j < a; j++) {
        matrix[j] = [];
        for (var i = 0; i < a; i++) {
            matrix[j][i] = 0;
        }
    }
    for (var k = 0; k < a; k++) {
        matrix[k][(a-1-k)] = 1;
    }
    console.log(matrix);
}

matrixer(10);
