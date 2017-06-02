'use strict'

var BackendServer = (function() {

    function init() {
        const mysql = require('mysql');
        const express = require('express');
        const bodyParser = require('body-parser');
        const app = express();

        app.use(bodyParser.json());

        app.use('/assets', express.static('assets'))

        var conn = mysql.createConnection({
            host: "localhost",
            user: "'Fekapapa'",
            password: "1q2w3ezv8ta4",
            database: "musicplayer"
        });

        app.get('/', function(req, res) {
            res.sendFile(__dirname + '/musicplayer_2.html');
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

        getPlaylists(app, conn);
        getCurrentTracks(app, conn);
        putFavoritePlus(app, conn);
        putFavoriteMinus(app, conn);
    }

    function getPlaylists(app, conn) {
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
    }

    // function postPlaylist () {
    //     app.post ('/playlists', function(req, res) {
    //         var query = 'INSERT INTO playlists (title, system) VALUES ("'
    //          + req.body.title + '", "' + req.body.system + '")';
    //         conn.query(query), function(err,rows){
    //         };
    //     });
    // }

    function getCurrentTracks(app, conn) {
        app.get('/tracks', function(req, res) {
            conn.query('SELECT * FROM tracks', function(err,rows){
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
    }

    function putFavoritePlus(app, conn) {
        app.put ('/tracksfavplus', function(req, res) {
            var query = 'UPDATE tracks SET favorite=1 WHERE title = ' + '"' + req.body.title + '"';
            console.log(query);
            conn.query(query), function(err,rows){
            };
        });
    }

    function putFavoriteMinus(app, conn) {
        app.put ('/tracksfavminus', function(req, res) {
            var query = 'UPDATE tracks SET favorite=0 WHERE title = ' + '"' + req.body.title + '"';
            console.log(query);
            conn.query(query), function(err,rows){
            };
        });
    }

    return {
        init: init
    }

})();

BackendServer.init();
