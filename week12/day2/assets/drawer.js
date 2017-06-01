'use strict'

var drawer = (function() {

    function playlistDrawer () {
        var playlists = playlists;
        var playlistbox = document.querySelector('.playlistbox');

        for (let i = 1; i < playlists.length; i++) {

            var onelistcont = document.createElement('div');
            playlistbox.appendChild(onelistcont);
            onelistcont.setAttribute('class', 'onelist type' + ((i % 2) + 1));
            onelistcont.addEventListener('click', coloredListElem);

            var listbox = document.createElement('div');
            onelistcont.appendChild(listbox);
            listbox.innerHTML = playlists[i].title;
            listbox.setAttribute('class', 'listbox');

            var listex = document.createElement('div');
            onelistcont.appendChild(listex);
            listex.innerHTML = '&#10006';
            listex.setAttribute('class', 'listex');
        }
    }

    function tracklistDrawer () {

    }

    function onelistHighlight () {

    }

    function onesongHighlight () {

    }

    function favoriteIconHighlight () {

    }

    function shuffleHighlight () {

    }

    function currentSongDisplay () {

    }

    function currentSongsArtistDisplay () {

    }

    function playButtonDisplay () {

    }

    function pauseButtonDisplay () {

    }

    function seekbarDisplay () {

    }

    function volumebarDisplay () {

    }

    return {
        // nameContainer: nameContainer
    }

})();
