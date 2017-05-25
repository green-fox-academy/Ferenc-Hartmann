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
	{ "id": 1, "title": "Drift", "artist": "Untitled artist", "duration": 209, "path": "style/drift.mp3" },

    { "id": 2, "title": "AK47", "artist": "Pisti", "duration": 2, "path": "style/AK47.mp3" },
    { "id": 3, "title": "Double Barrel Shotgun Firing", "artist": "Jozsó", "duration": 2, "path": "style/Double Barrel Shotgun Firing.mp3" },
    { "id": 4, "title": "Grenade", "artist": "Marcsi", "duration": 2, "path": "style/Grenade.mp3" },
    { "id": 5, "title": "M1 Garand Single", "artist": "Erős Vulkán", "duration": 2, "path": "style/M1 Garand Single.mp3" },
    { "id": 6, "title": "Swords Clashing", "artist": "Artúr", "duration": 2, "path": "style/Swords Clashing.mp3" },
    { "id": 7, "title": "Tank firing", "artist": "Tankerman", "duration": 2, "path": "style/Tank firing.mp3" },
    { "id": 8, "title": "Uzi Shooting", "artist": "GTA 5", "duration": 2, "path": "style/Uzi Shooting.mp3" },
    ]
    res.send(tracks);
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/music.html');
});


app.listen(3000, function () {
    console.log('server running');
});
