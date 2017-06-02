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

    }

    function shuffleClicked() {
// If active it must be blue
    }

    function volumeClicked() {

    }

    function volumebarClicked() {

    }

    function favoriteClicked() {
// The star is immediately turned to light blue
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
        endChacker: endChacker
    }

})();
