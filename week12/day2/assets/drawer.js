'use strict'

var drawer = (function() {

    function playlistDrawer(playlists) {
        var playlists = playlists;
        var playlistbox = document.querySelector('.playlistbox');

        for (let i = 1; i < playlists.length; i++) {

            var onelistcont = document.createElement('div');
            playlistbox.appendChild(onelistcont);
            onelistcont.setAttribute('class', 'onelist');
            // onelistcont.addEventListener('click', coloredListElem);

            var listbox = document.createElement('div');
            onelistcont.appendChild(listbox);
            listbox.innerHTML = playlists[i].title;
            listbox.setAttribute('class', 'listbox');

            var listex = document.createElement('span');
            onelistcont.appendChild(listex);
            listex.innerHTML = '&#10006';
            listex.setAttribute('class', 'listex');
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
            // onesongcont.addEventListener('click', coloredTrackelem);

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
        tracklistDrawer: tracklistDrawer
    }

})();
