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
// SELECT book_name, aut_name FROM book_mast JOIN author ON aut_id = book_mast.aut_id


app.get('/', function(req, res) {
  conn.query("SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast LEFT JOIN author ON book_mast.aut_id = author.aut_id LEFT JOIN category ON book_mast.cate_id = category.cate_id LEFT JOIN publisher ON book_mast.pub_id = publisher.pub_id", function(err,rows){
      if(err){
        console.log("Error connecting to Db");
        console.log(err);
  }else {
        console.log("Data received from Db:\n");
        var html = '<table>' + '<tr><th>book title</th>' + '<th>authors name</th>' + '<th>category</th>' + '<th>publishers name</th>' + '<th>price (USD)</th></tr>';
        for (var i = 0; i < rows.length; i++) {
            html = html + '<tr><td>' + (rows[i].book_name) + '</td><td>' + (rows[i].aut_name) + '</td><td>' + (rows[i].cate_descrip) + '</td><td>' + (rows[i].pub_name) + '</td><td>' + (rows[i].book_price) + '</td></tr>';
        }
        html = html + '</table>';
        console.log(rows);
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
