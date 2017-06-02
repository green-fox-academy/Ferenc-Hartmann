'use strict'

var InputHandler = (function() {

    function logoClicked() {
        console.log('logoClicked');
    }

    function newPlaylistClicked() {
        console.log('newPlaylistClicked');
    }

    function onelistClicked() {
        console.log('onelistClicked');
    }

    function onesongClicked() {
        console.log('onesongClicked');
    }

    function previousSongClicked() {
        Controller.trackChange(-1);
    }

    function playClicked() {
        Drawer.audio.play();
    }

    function pauseClicked() {
        Drawer.audio.pause();
    }

    function nextSongClicked() {
        Controller.trackChange(+1);
    }

    function seekbarClicked() {
         Controller.seekbarClicked();
    }

    function shuffleClicked() {
        console.log('shuffleClicked');
// If active it must be blue
    }

    function volumeClicked() {
        console.log('volumeClicked');
    }

    function volumebarClicked() {
        console.log('volumebarClicked');
    }

    function favoriteClicked() {
        Controller.favoriteClicked();
    }

    function addtoPlaylistClicked() {
        console.log('addtoPlaylistClicked');
    }

    function deletePlaylistClicked() {
        console.log('deletePlaylistClicked');
    }

    function spaceKeyPressed() {
        console.log('spaceKeyPressed');
    }

    function nKeyPressed() {
        console.log('nKeyPressed');
    }

    function pKeyPressed() {
        console.log('pKeyPressed');
    }

    function escKeyPressed() {
        console.log('escKeyPressed');
    }

    return {
        logoClicked: logoClicked,
        newPlaylistClicked: newPlaylistClicked,
        onelistClicked: onelistClicked,
        onesongClicked: onesongClicked,
        previousSongClicked: previousSongClicked,
        playClicked: playClicked,
        pauseClicked: pauseClicked,
        nextSongClicked: nextSongClicked,
        seekbarClicked: seekbarClicked,
        shuffleClicked: shuffleClicked,
        volumeClicked: volumeClicked,
        volumebarClicked: volumebarClicked,
        favoriteClicked: favoriteClicked,
        addtoPlaylistClicked: addtoPlaylistClicked,
        deletePlaylistClicked: deletePlaylistClicked,
        spaceKeyPressed: spaceKeyPressed,
        nKeyPressed: nKeyPressed,
        pKeyPressed: pKeyPressed,
        escKeyPressed: escKeyPressed
    }

})();
