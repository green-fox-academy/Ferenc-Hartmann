'use strict'

var Controller = (function() {

    function init() {
        FrontendServer.getPlaylists();
        FrontendServer.getCurrentTracks();
        Drawer.staticHtmlEventListeners();
    }

    function playlistDataRouter(playlists) {
        Drawer.playlistDrawer(playlists);
    }

    function trackDataRouter(tracks) {
        Drawer.tracklistDrawer(tracks);
        InnerProcessor.audioSource(tracks);
    }

    function eventListenerRouter(element, action) {
        InnerProcessor.eventListenAdder(element, action);
    }

    function onChangeRouter(element, action) {
        InnerProcessor.onChangeAdder(element, action);
    }

    function play() {
        Drawer.pauseButtonDisplay();
        InputHandler.playClicked();
    }

    function pause() {
        Drawer.playButtonDisplay();
        InputHandler.pauseClicked();
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
        eventListenerRouter: eventListenerRouter,
        onChangeRouter: onChangeRouter,
        play: play,
        pause: pause
    }

})();

Controller.init();
