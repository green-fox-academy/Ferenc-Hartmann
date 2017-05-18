'use strict'

const mysql = require("mysql");
const express = require('express');
const app = express();

var conn = mysql.createConnection({
  host: "localhost",
  user: "'Fekapapa'",
  password: "1q2w3ezv8ta4",
  database: "bookstore"
});

// var country = "USA";
// var city = "Atlanta";
//
// const query = {
//     sql: "SELECT * FROM author WHERE country = ? AND home_city = ?",
//     values: [country, city]
// }

app.get('/', function(req, res) {
    var result = [];
  conn.query("SELECT book_name FROM book_mast", function(err,rows){
      if(err){
        console.log("Error connecting to Db");
  }else {
        console.log("Data received from Db:\n");
        var html = '<ul>';
        for (var i = 0; i < rows.length; i++) {
            html = html + '<li>' + (rows[i].book_name) + '</li>';
        }
        html = html + '</ul>';
  }
  res.send(html);
  });
});

app.listen(3000, function () {
    console.log('server running');
});


conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});
