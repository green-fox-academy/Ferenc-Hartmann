'use strict';

var playlistGenerator = function(playlists) {
    var playlists = playlists;
    var playlistbox = document.querySelector('.playlistbox');

    for (let i = 1; i < playlists.length; i++) {

        var onelistcont = document.createElement('div');
        playlistbox.appendChild(onelistcont);
        onelistcont.setAttribute('class', 'onelist');
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

var songbox = document.querySelector('.songbox');

var songListGenerator = function(tracks) {
    var tracks = tracks;

    songbox.innerHTML = '';

    for (let i = 0; i < tracks.length; i++) {

        let time = timeManagement(tracks[i].duration, i);

        var onesongcont = document.createElement('div');
        songbox.appendChild(onesongcont);
        onesongcont.setAttribute('class', 'onesong');
        onesongcont.addEventListener('click', coloredTrackelem);

        var ordernumber = document.createElement('div');
        onesongcont.appendChild(ordernumber);
        ordernumber.innerHTML = i + 1;
        ordernumber.setAttribute('class', 'ordernumber');

        var title = document.createElement('div');
        onesongcont.appendChild(title);
        title.innerHTML = tracks[i].title;
        title.setAttribute('class', 'title');

        var length = document.createElement('div');
        onesongcont.appendChild(length);
        length.innerHTML = time;
        length.setAttribute('class', 'length');
    }
    staticHtmlSelector();
}
