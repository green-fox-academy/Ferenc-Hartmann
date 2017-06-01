'use strict'

var innerProcessor = (function() {

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

    function playClicked() {

    }

    function pauseClicked() {

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
        eventListenAdder: eventListenAdder
    }

})();
