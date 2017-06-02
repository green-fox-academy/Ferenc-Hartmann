'use strict'

var Drawer = (function() {

    function playlistDrawer(playlists) {
        var playlists = playlists;
        var playlistbox = document.querySelector('.playlistbox');
        var allTracks = document.querySelector('.onelist.tracks');
        var favorites = document.querySelector('.onelist.favorites');
        Controller.eventListenerRouter(allTracks, InputHandler.onelistClicked);
        Controller.eventListenerRouter(favorites, InputHandler.onelistClicked);

        for (let i = 1; i < playlists.length; i++) {

            var onelistcont = document.createElement('div');
            playlistbox.appendChild(onelistcont);
            onelistcont.setAttribute('class', 'onelist');

            var listbox = document.createElement('div');
            onelistcont.appendChild(listbox);
            listbox.innerHTML = playlists[i].title;
            listbox.setAttribute('class', 'listbox');
            Controller.eventListenerRouter(listbox, InputHandler.onelistClicked);

            var listex = document.createElement('span');
            onelistcont.appendChild(listex);
            listex.innerHTML = '&#10006';
            listex.setAttribute('class', 'listex');
            Controller.eventListenerRouter(listex, InputHandler.deletePlaylistClicked);
        }
    }

    function tracklistDrawer(tracks) {

        var tracks = tracks;

        Drawer.songbox.innerHTML = '';

        for (let i = 0; i < tracks.length; i++) {

            let time = Controller.timeRouter(tracks[i].duration);

            var onesongcont = document.createElement('div');
            Drawer.songbox.appendChild(onesongcont);
            onesongcont.setAttribute('class', 'onesong');
            Controller.eventListenerRouter(onesongcont, InputHandler.onesongClicked);

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
        var logo = document.querySelector('.logo');
        var rewind = document.querySelector('.rewind');
        var forward = document.querySelector('.forward');
        var seekbarInput = document.querySelector('input:nth-child(5)');
        var shuffle = document.querySelector('.shuffle');
        var volume = document.querySelector('.volumeimg');
        var volumebarInput = document.querySelector('input:nth-child(9)');
        var titleholder = document.querySelector('.titleholder');
        var artistholder = document.querySelector('.artistholder');
        var favorite = document.querySelector('.star');
        var plus = document.querySelector('.plus');
        var adder = document.querySelector('.adder');

        Controller.eventListenerRouter(logo, InputHandler.logoClicked);
        Controller.eventListenerRouter(this.playButton, InnerProcessor.playPause);
        Controller.eventListenerRouter(rewind, InputHandler.previousSongClicked);
        Controller.eventListenerRouter(forward, InputHandler.nextSongClicked);
        Controller.onChangeRouter(seekbarInput, InputHandler.seekbarClicked);
        Controller.eventListenerRouter(shuffle, InputHandler.shuffleClicked);
        Controller.eventListenerRouter(volume, InputHandler.volumeClicked);
        Controller.onChangeRouter(volumebarInput, InputHandler.volumebarClicked);
        Controller.eventListenerRouter(favorite, InputHandler.favoriteClicked);
        Controller.eventListenerRouter(plus, InputHandler.addtoPlaylistClicked);
        Controller.eventListenerRouter(adder, InputHandler.newPlaylistClicked);
    }

    function onelistHighlight() {

    }

    function onesongHighlight() {
        var rowNumber = InnerProcessor.currentSong + 1;
        var currentRow = Drawer.songbox.querySelector('div:nth-child(' + rowNumber + ')');

        for (let i = 1; i <= Controller.tracks.length; i++) {
            if (i % 2 === 1) {
                Drawer.songbox.querySelector('div:nth-child(' + i + ')').setAttribute('style', 'background-color: rgb(234, 234, 234);')
            } else if (i % 2 === 0){
                Drawer.songbox.querySelector('div:nth-child(' + i + ')').setAttribute('style', 'background-color: rgb(245, 245, 245);')
            }
        }
        currentRow.setAttribute('style', 'background-color: rgb(170, 230, 230);')
    }

    function remainTimeDrawer() {
        var remaintime = document.querySelector('.remaintime');
        remaintime.innerHTML = Controller.timeRouter(Controller.tracks[InnerProcessor.currentSong].duration - Math.floor(Drawer.audio.currentTime));
    }

    function totalLengthDrawer() {
        var totallength = document.querySelector('.totallength');
        totallength.innerHTML = Controller.timeRouter(Controller.tracks[InnerProcessor.currentSong].duration);
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
        this.playButton.setAttribute('style', 'background-image: url(assets/images/play.svg);');
    }

    function pauseButtonDisplay() {
        this.playButton.setAttribute('style', 'background-image: url(assets/images/pause.svg);');
    }

    function seekbarDisplay() {

    }

    function volumebarDisplay() {

    }

    return {
        playlistDrawer: playlistDrawer,
        tracklistDrawer: tracklistDrawer,
        staticHtmlEventListeners: staticHtmlEventListeners,
        audio: document.querySelector('audio'),
        playButton: document.querySelector('.play'),
        songbox: document.querySelector('.songbox'),
        pauseButtonDisplay: pauseButtonDisplay,
        playButtonDisplay: playButtonDisplay,
        onesongHighlight: onesongHighlight,
        totalLengthDrawer: totalLengthDrawer,
        remainTimeDrawer: remainTimeDrawer
    }

})();
