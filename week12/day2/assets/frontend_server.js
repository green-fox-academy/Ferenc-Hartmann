'use strict'

var frontendServer = (function() {

    function getPlaylists() {
        var http = new XMLHttpRequest();
        http.onreadystatechange = function() {
            if (http.readyState === 4 && http.status === 200) {
                var playlists = JSON.parse(http.response);
            }
        }
        http.open('GET', 'http://localhost:3000/playlists');
        http.send();
    }

    // function postPlaylists () {
    //
    // }

    function getCurrentTracks() {
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

    }

    function favoriteClicked() {
        var favoritePlus = function(title) {
            var http = new XMLHttpRequest();
            var data = {
                'title': title,
            }
            http.open('PUT', 'http://localhost:3000/tracksfavplus');
            http.setRequestHeader('Content-Type', 'application/json');
            http.send(JSON.stringify(data));
        };
    }

    function favoriteUnclicked() {
        var favoriteMinus = function(title) {
            var http = new XMLHttpRequest();
            var data = {
                'title': title,
            }
            http.open('PUT', 'http://localhost:3000/tracksfavminus');
            http.setRequestHeader('Content-Type', 'application/json');
            http.send(JSON.stringify(data));
        };
    }

    return {
        getPlaylists: getPlaylists,
        getCurrentTracks: getCurrentTracks,
        favoriteClicked: favoriteClicked,
        favoriteUnclicked: favoriteUnclicked
    }

})();
