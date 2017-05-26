'use strict'

const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

app.use('/style', express.static('style'))

var conn = mysql.createConnection({
    host: "localhost",
    user: "'Fekapapa'",
    password: "1q2w3ezv8ta4",
    database: "musicplayer"
});

app.get('/playlists', function(req, res) {
    conn.query('SELECT * FROM playlists', function(err,rows){
        if(err){
            console.log("Error connecting to Db");
            console.log(err);
        }else {
            console.log("Data received from Db:\n");
            console.log(rows);
        };
    res.send(rows);
    });
});

app.post ('/playlists', function(req, res) {
    var query = 'INSERT INTO playlists (title, system) VALUES ("'
     + req.body.title + '", "' + req.body.system + '")';
    conn.query(query), function(err,rows){
    };
});


app.get('/tracks', function(req, res) {
    conn.query('SELECT * FROM tracks', function(err,rows){
        if(err){
            console.log("Error connecting to Db");
            console.log(err);
        }else {
            console.log("Data received from Db:\n");
        };
    res.send(rows);
    });
});

app.post ('/tracks', function(req, res) {
    var query = 'INSERT INTO tracks (title, artist, path, duration, favorite, playlist) VALUES ("'
     + req.body.title + '", "' + req.body.artist + '", "' + req.body.path + '", "' + req.body.duration + '", "' + req.body.favorite + '", "' + req.body.playlist + '")';
     console.log(query);
    conn.query(query), function(err,rows){
    };
});

app.post ('/tracksdel', function(req, res) {
    var query = 'DELETE FROM tracks WHERE id = ' + req.body.id;
    console.log(query);
    conn.query(query), function(err,rows){
    };
});

app.put ('/tracksfavplus', function(req, res) {
    var query = 'UPDATE tracks SET favorite=1 WHERE id = ' + req.body.id;
    console.log(query);
    conn.query(query), function(err,rows){
    };
});

app.put ('/tracksfavminus', function(req, res) {
    var query = 'UPDATE tracks SET favorite=0 WHERE id = ' + req.body.id;
    console.log(query);
    conn.query(query), function(err,rows){
    };
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/music.html');
});

app.listen(3000, function () {
    console.log('server running');
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
    };
    console.log("Connection established");
});
