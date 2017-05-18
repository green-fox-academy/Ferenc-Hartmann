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

app.get('/', function(req, res) {
    var category = '';
    var publisher = '';
    var plt = '';
    var pgt = '';

    if (req.query.category !== undefined) {
        category = 'category.cate_descrip = ' + '"' + req.query.category + '" AND ';
    }
    if (req.query.publisher !== undefined) {
        publisher = 'pub_name = ' + '"' + req.query.publisher + '" AND ';
    }
    if (req.query.plt !== undefined) {
        plt = 'book_price < ' + '"' + req.query.plt + '" AND ';
    }
    if (req.query.pgt !== undefined) {
        pgt = 'book_price > ' + '"' + req.query.pgt + '" AND ';
    }

    if (category === '' && publisher === '' && plt === '' && pgt === '') {
        var filter = '';
    }else {
        filter = ' WHERE ' + category + publisher + plt + pgt;
        filter = filter.slice(0, -5);
    }

    var query = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast LEFT JOIN author ON book_mast.aut_id = author.aut_id LEFT JOIN category ON book_mast.cate_id = category.cate_id LEFT JOIN publisher ON book_mast.pub_id = publisher.pub_id' + filter;
    console.log (query);
  conn.query(query, function(err,rows){
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
