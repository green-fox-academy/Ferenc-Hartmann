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

// app.get('/playlists', function(req, res) {
//     var playlists = [
// 	{ "id": 1, "title": "Favorites", "system": 1},
// 	{ "id": 2, "title": "Music for programming", "system": 0},
// 	{ "id": 3, "title": "Driving", "system": 0},
// 	{ "id": 5, "title": "Fox house", "system": 0},
//     ]
//     res.send(playlists);
// });

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

// app.get('/tracks', function(req, res) {
//     var tracks= [
// 	{ "id": 1, "title": "Drift", "artist": "Untitled artist", "duration": 209, "path": "style/drift.mp3" },
//
//     { "id": 2, "title": "AK47", "artist": "Pisti", "duration": 2, "path": "style/AK47.mp3" },
//     { "id": 3, "title": "Double Barrel Shotgun Firing", "artist": "Jozsó", "duration": 2, "path": "style/Double Barrel Shotgun Firing.mp3" },
//     { "id": 4, "title": "Grenade", "artist": "Marcsi", "duration": 2, "path": "style/Grenade.mp3" },
//     { "id": 5, "title": "M1 Garand Single", "artist": "Erős Vulkán", "duration": 2, "path": "style/M1 Garand Single.mp3" },
//     { "id": 6, "title": "Swords Clashing", "artist": "Artúr", "duration": 2, "path": "style/Swords Clashing.mp3" },
//     { "id": 7, "title": "Tank firing", "artist": "Tankerman", "duration": 2, "path": "style/Tank firing.mp3" },
//     { "id": 8, "title": "Uzi Shooting", "artist": "GTA 5", "duration": 2, "path": "style/Uzi Shooting.mp3" },
//     ]
//     res.send(tracks);
// });

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
