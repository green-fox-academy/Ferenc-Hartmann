'use strict'

var InnerProcessor = (function() {

    function timeManagement(duration) {
        if (duration > 60) {
            var minuteMan = Math.floor(duration / 60) + ':' + Math.floor(duration % 60);
            if (Math.floor(duration % 60)  < 10) {
                minuteMan = Math.floor(duration / 60) + ':0' + Math.floor(duration % 60);
            }
        } else {
            var minuteMan = Math.floor(duration);
        }
        return minuteMan
    }

    function eventListenAdder(element, action) {
        element.addEventListener('click', action);
    }

    function playPause() {
        if (Drawer.audio.paused === false) {
            Controller.pauseClicked();
        }
        else if (Drawer.audio.paused === true) {
            Controller.playClicked();
        }
    }

    function trackSwitcher(value, tracks) {
        if (value === 'init') {
            InnerProcessor.currentSong = 0;
            Drawer.audio.setAttribute('src', tracks[InnerProcessor.currentSong].path);
        } else if (value === -1 && InnerProcessor.currentSong > 0) {
            InnerProcessor.currentSong--;
        } else if (value === -1 && InnerProcessor.currentSong === 0) {
            InnerProcessor.currentSong = (tracks.length - 1);
        } else if (value === +1 && InnerProcessor.currentSong < (tracks.length - 1)) {
            InnerProcessor.currentSong++;
        } else if (value === +1 && InnerProcessor.currentSong === (tracks.length - 1)) {
            InnerProcessor.currentSong = 0;
        }

        Drawer.audio.setAttribute('src', tracks[InnerProcessor.currentSong].path);
    }

    function endChacker() {
        if (Drawer.audio.ended === true) {
            Controller.trackChange(+1);
            playPause();
        }
    }

    function onChangeAdder(element, action) {
        element.onchange = action;
    }

    function interval() {
        var interval = setInterval(Controller.intervalCaller, 1000);
    }

    function playlistDrawer() {

    }

    function tracklistDrawer() {

    }

    function logoClicked() {

    }

    function newPlaylistClicked() {

    }

    function onelistClicked() {

    }

    function onesongClicked() {

    }

    function previousSongClicked() {

    }

    function nextSongClicked() {

    }

    function seekbarClicked() {
        Drawer.audio.currentTime = Drawer.seekbarInput.value / 100 * Controller.tracks[InnerProcessor.currentSong].duration;
    }

    function shuffleClicked() {
// If active it must be blue
    }

    function volumeClicked() {

    }

    function volumebarClicked() {

    }

    function favoriteClicked() {
        if (Controller.tracks[InnerProcessor.currentSong].favorite === 0) {
            Controller.setFavorite(Controller.tracks[InnerProcessor.currentSong].title);
            Controller.tracks[InnerProcessor.currentSong].favorite = 1;
        } else if (Controller.tracks[InnerProcessor.currentSong].favorite === 1) {
            Controller.unsetFavorite(Controller.tracks[InnerProcessor.currentSong].title);
            Controller.tracks[InnerProcessor.currentSong].favorite = 0;
        }
    }

    function favoriteCheck() {
        if (Controller.tracks[InnerProcessor.currentSong].favorite === 0) {
            Controller.favoriteChecked(Drawer.favoriteIconNormal());
        } else {
            Controller.favoriteChecked(Drawer.favoriteIconHighlight());

        }

    }

    function addtoPlaylistClicked() {

    }

    function deletePlaylistClicked() {

    }

    function spaceKeyPressed() {

    }

    function nKeyPressed() {

    }

    function pKeyPressed() {

    }

    function escKeyPressed() {

    }

    function seekbarProgress() {
        Drawer.seekbarInput.value = (Drawer.audio.currentTime / Controller.tracks[InnerProcessor.currentSong].duration) * 100;

    }

    function nextSongCalculator() {

    }

    return {
        timeManagement: timeManagement,
        eventListenAdder: eventListenAdder,
        onChangeAdder: onChangeAdder,
        playPause: playPause,
        trackSwitcher: trackSwitcher,
        currentSong: 0,
        interval: interval,
        endChacker: endChacker,
        seekbarProgress: seekbarProgress,
        seekbarClicked: seekbarClicked,
        favoriteClicked: favoriteClicked,
        favoriteCheck: favoriteCheck
    }

})();
