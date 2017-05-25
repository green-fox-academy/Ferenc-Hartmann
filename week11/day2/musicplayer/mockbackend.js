'use strict'

const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

app.use('/style', express.static('style'))

app.get('/playlists', function(req, res) {
    var playlists = [
	{ "id": 1, "title": "Favorites", "system": 1},
	{ "id": 2, "title": "Music for programming", "system": 0},
	{ "id": 3, "title": "Driving", "system": 0},
	{ "id": 5, "title": "Fox house", "system": 0},
    ]
    res.send(playlists);
});

app.get('/tracks', function(req, res) {
    var tracks= [
	{ "id": 21, "title": "Drift", "artist": "Untitled artist", "duration": 200, "path": "style/drift.mp3" },
	{ "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "style/drift2.mp3" }
    ]
    res.send(tracks);
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/music.html');
});


app.listen(3000, function () {
    console.log('server running');
});
