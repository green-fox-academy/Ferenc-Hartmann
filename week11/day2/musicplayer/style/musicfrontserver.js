'use strict';

// Server control: getting playlists

var http = new XMLHttpRequest();

http.onreadystatechange = function() {
    if (http.readyState === 4 && http.status === 200) {
        var playlists = JSON.parse(http.response);
        playlistGenerator(playlists);
    }
}
http.open('GET', 'http://localhost:3000/playlists');
http.send();


var trackCall = function() {
    var getTrack = new XMLHttpRequest();
    getTrack.onreadystatechange = function() {
        if (getTrack.readyState === 4 && getTrack.status === 200) {
            var tracks = JSON.parse(getTrack.response);
            songListGenerator(tracks);
            AudioControl(tracks);
        }
    }
    getTrack.open('GET', 'http://localhost:3000/tracks');
    getTrack.send();
};

var favoriteCall = function() {
    var getFavorite = new XMLHttpRequest();
    getFavorite.onreadystatechange = function() {
        if (getFavorite.readyState === 4 && getFavorite.status === 200) {
            var tracks = JSON.parse(getFavorite.response);
            songListGenerator(tracks);
            AudioControl(tracks);
        }
    }
    getFavorite.open('GET', 'http://localhost:3000/favorites');
    getFavorite.send();
}

var favoritePlus = function() {
    var http = new XMLHttpRequest();

    var data = {
        "title": "Grenade",
        "favorite": "1"
    }

    http.open('PUT', 'http://localhost:3000/tracksfavplus');
    http.setRequestHeader('Content-Type', 'application/json');
    http.send(JSON.stringify(data));
};

var favoriteMinus = function() {
    var http = new XMLHttpRequest();

    var data = {
        "id": "10",
        "favorite": "0"
    }

    http.open('PUT', 'http://localhost:3000/tracksfavminus');
    http.setRequestHeader('Content-Type', 'application/json');
    http.send(JSON.stringify(data));
};

// function send() {
//     var http = new XMLHttpRequest();
//
//     var data = {
//         "title": "Uzi Shooting",
//         "artist": "GTA 9",
//         "path": "style/Uzi Shooting.mp3",
//         "duration": 2,
//         "favorite": 0,
//         "playlist": "Militarty Sound"}
//
//     http.open('POST', 'http://localhost:3000/tracks');
//     http.setRequestHeader('Content-Type', 'application/json');
//     http.send(JSON.stringify(data));
//     console.log(data);
// }
// send();

// function send() {
//     var http = new XMLHttpRequest();
//
//     var data = {
//         "title": "Military Sound",
//         "system": 0,
//     }
//     http.open('POST', 'http://localhost:3000/playlists');
//     http.setRequestHeader('Content-Type', 'application/json');
//     http.send(JSON.stringify(data));
// }
// send();

// function send() {
//     var http = new XMLHttpRequest();
//
//     var data = {
//         "id": "10",
//     }
//
//     http.open('POST', 'http://localhost:3000/tracksdel');
//     http.setRequestHeader('Content-Type', 'application/json');
//     http.send(JSON.stringify(data));
// }
// send();
