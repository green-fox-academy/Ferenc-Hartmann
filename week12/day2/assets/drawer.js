'use strict'

var drawer = (function() {

    function playlistDrawer(playlists) {
        var playlists = playlists;
        var playlistbox = document.querySelector('.playlistbox');
        var allTracks = document.querySelector('.onelist.tracks');
        var favorites = document.querySelector('.onelist.favorites');
        controller.eventListenerRouter(allTracks, inputHandler.onelistClicked);
        controller.eventListenerRouter(favorites, inputHandler.onelistClicked);

        for (let i = 1; i < playlists.length; i++) {

            var onelistcont = document.createElement('div');
            playlistbox.appendChild(onelistcont);
            onelistcont.setAttribute('class', 'onelist');

            var listbox = document.createElement('div');
            onelistcont.appendChild(listbox);
            listbox.innerHTML = playlists[i].title;
            listbox.setAttribute('class', 'listbox');
            controller.eventListenerRouter(listbox, inputHandler.onelistClicked);

            var listex = document.createElement('span');
            onelistcont.appendChild(listex);
            listex.innerHTML = '&#10006';
            listex.setAttribute('class', 'listex');
            controller.eventListenerRouter(listex, inputHandler.deletePlaylistClicked);
        }
    }

    function tracklistDrawer(tracks) {

        var tracks = tracks;
        var songbox = document.querySelector('.songbox');

        songbox.innerHTML = '';

        for (let i = 0; i < tracks.length; i++) {

            let time = innerProcessor.timeManagement(tracks[i].duration);

            var onesongcont = document.createElement('div');
            songbox.appendChild(onesongcont);
            onesongcont.setAttribute('class', 'onesong');
            controller.eventListenerRouter(onesongcont, inputHandler.onesongClicked);

            var ordernumber = document.createElement('span');
            onesongcont.appendChild(ordernumber);
            ordernumber.innerHTML = i + 1;
            ordernumber.setAttribute('class', 'ordernumber');

            var title = document.createElement('span');
            onesongcont.appendChild(title);
            title.innerHTML = tracks[i].title;
            title.setAttribute('class', 'title');

            var length = document.createElement('span');
            onesongcont.appendChild(length);
            length.innerHTML = time;
            length.setAttribute('class', 'length');
        }
    }

    function staticHtmlEventListeners() {
        var audio = document.querySelector('audio');
        var logo = document.querySelector('.logo');
        var playButton = document.querySelector('.play');
        var rewind = document.querySelector('.rewind');
        var forward = document.querySelector('.forward');
        var remaintime = document.querySelector('.remaintime');
        var seekbarInput = document.querySelector('input:nth-child(5)');
        var totallength = document.querySelector('.totallength');
        var shuffle = document.querySelector('.shuffle');
        var volume = document.querySelector('.volumeimg');
        var volumebarInput = document.querySelector('input:nth-child(9)');
        var titleholder = document.querySelector('.titleholder');
        var artistholder = document.querySelector('.artistholder');
        var favorite = document.querySelector('.star');
        var plus = document.querySelector('.plus');
        var adder = document.querySelector('.adder');

        controller.eventListenerRouter(logo, inputHandler.logoClicked);
        controller.eventListenerRouter(playButton, inputHandler.playClicked);
        controller.eventListenerRouter(rewind, inputHandler.previousSongClicked);
        controller.eventListenerRouter(forward, inputHandler.nextSongClicked);
        controller.onChangeRouter(seekbarInput, inputHandler.seekbarClicked);
        controller.eventListenerRouter(shuffle, inputHandler.shuffleClicked);
        controller.eventListenerRouter(volume, inputHandler.volumeClicked);
        controller.onChangeRouter(volumebarInput, inputHandler.volumebarClicked);
        controller.eventListenerRouter(favorite, inputHandler.favoriteClicked);
        controller.eventListenerRouter(plus, inputHandler.addtoPlaylistClicked);
        controller.eventListenerRouter(adder, inputHandler.newPlaylistClicked);


    }

    function onelistHighlight() {

    }

    function onesongHighlight() {

    }

    function favoriteIconHighlight() {

    }

    function shuffleHighlight() {

    }

    function currentSongDisplay() {

    }

    function currentSongsArtistDisplay() {

    }

    function playButtonDisplay() {

    }

    function pauseButtonDisplay() {

    }

    function seekbarDisplay() {

    }

    function volumebarDisplay() {

    }

    return {
        playlistDrawer: playlistDrawer,
        tracklistDrawer: tracklistDrawer,
        staticHtmlEventListeners: staticHtmlEventListeners
    }

})();
