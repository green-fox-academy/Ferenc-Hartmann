'use strict'

var controller = (function() {

    function init() {
        frontendServer.getPlaylists();
        frontendServer.getCurrentTracks();
    }

    function playlistDataRouter(playlists) {
        drawer.playlistDrawer(playlists);
    }

    function trackDataRouter(tracks) {
        drawer.tracklistDrawer(tracks);
    }

    function eventListenerRouter(element, action) {
        innerProcessor.eventListenAdder(element, action);
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

    return {
        init: init,
        playlistDataRouter: playlistDataRouter,
        trackDataRouter: trackDataRouter,
        eventListenerRouter: eventListenerRouter
    }

})();

controller.init();
