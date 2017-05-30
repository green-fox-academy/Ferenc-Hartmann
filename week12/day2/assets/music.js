'use strict';

var timeManagement = function(duration, i) {
    if (duration > 60) {
        var minuteMan = Math.floor(duration / 60) + ':' + Math.floor(duration % 60);
        if (Math.floor(duration % 60)  < 10) {
            minuteMan = Math.floor(duration / 60) + ':0' + Math.floor(duration % 60);
        }
    } else {
        var minuteMan = Math.floor(duration);
    }
    return minuteMan
};

var staticHtmlSelector = function() {
    var standard1 = document.querySelector('.standard1');
    var standard2 = document.querySelector('.standard2');
    standard1.addEventListener('click', eventRouter);
    standard2.addEventListener('click', eventRouter2);
};

var eventRouter = function(e) {
    var playListBox = document.querySelectorAll('.playlistbox>div');
    document.getElementsByClassName(playListBox[0].setAttribute('class', "onelist type2 standard1 selected"));
    coloredListElem(e);
    getAllTrack();
};

var eventRouter2 = function(e) {
    coloredListElem(e);
    getfavorite();
};

var coloredTrackelem = function(e) {
    var songList = document.querySelectorAll('.songbox>div');
    try {
        for (let i = 0; i < 2; i++) {
            let elements = document.getElementsByClassName(songList[i].getAttribute("class"));
            console.log(elements);
            for (let i = 0; i < elements.length; i++) {
                if (elements[i].className === 'onesong2 selected') {
                    elements[i].className = 'onesong2';
                }
                if (elements[i].className === 'onesong1 selected') {
                    elements[i].className = 'onesong1';
                }
            }
        }
    }
    catch(err) {
        console.log(err);
    }
    if (e.target.parentNode.className === 'onesong1' || e.target.parentNode.className === 'onesong2') {
        let color = e.target.parentElement;
        color.setAttribute('class', color.getAttribute('class') + ' selected');
    }
}

var coloredListElem = function(e) {
    var playListBox = document.querySelectorAll('.playlistbox>div');
    try {
        for (let i = 0; i < playListBox.length; i++) {
            let elements = document.getElementsByClassName(playListBox[i].getAttribute("class"));
            console.log(elements);
            console.log(playListBox.length);
            if (elements[0].className === 'onelist type2 standard1 selected') {
                elements[0].className = 'onelist type2 standard1';
            }
            if (elements[0].className === 'onelist type1 standard2 selected') {
                elements[0].className = 'onelist type1 standard2';
            }
            if (elements[0].className === 'onelist type2 selected') {
                elements[0].className = 'onelist type2';
            }
            if (elements[0].className === 'onelist type1 selected') {
                elements[0].className = 'onelist type1';
            }
        }
    }
    catch(err) {
        console.log(err);
    }

    if (e.target.parentNode.classList[0] === 'onelist') {
        let color = e.target.parentNode;
        color.setAttribute('class', color.getAttribute('class') + ' selected');
    }
    if (e.target.classList[2] === 'standard1') {
        let color = e.target.parentNode.querySelector('.standard1');
        color.setAttribute('class', color.getAttribute('class') + ' selected');
    }
    if (e.target.classList[2] === 'standard2') {
        let color = e.target.parentNode.querySelector('.standard2');
        color.setAttribute('class', color.getAttribute('class') + ' selected');
    }
};

var AudioControl = function(tracks) {
    var i = 0;
    var isPlay = 0;
    var counter = 0;
    var tracklist = tracks;
    var audio = document.querySelector('audio');
    var playButton = document.querySelector('.play');
    var rewind = document.querySelector('.rewind');
    var forward = document.querySelector('.forward');
    var remaintime = document.querySelector('.remaintime');
    var seekbarInput = document.querySelector('input:nth-child(5)');
    var totallength = document.querySelector('.totallength');
    var shuffle = document.querySelector('.shuffle');
    var volume = document.querySelector('.volumeimg');
    var volumebarInput = document.querySelector('input:nth-child(9)');
    var titleholder = document.querySelector('.titleholder');
    var artistholder = document.querySelector('.artistholder');
    var songList = document.querySelectorAll('.songbox>div');
    var playListBox = document.querySelectorAll('.playlistbox>div');
    titleholder.innerHTML = '--';
    artistholder.innerHTML = '--';
    var path = tracklist[i].path;
    var interval;
    var shuffleOn = false;
    var currentPlay = tracklist[i];
    audio.setAttribute('src', path);
    var previousTrack = 0;

    var playNextTrack = function() {
        if (audio.ended === true && shuffleOn === false) {
            i < tracklist.length - 1 ? i++ : i = 0;
            if (previousTrack != i) {
                songList[previousTrack].className = songList[previousTrack].className.slice(0, 8);
            }
            songList[i].className = songList[i].className + ' selected';
            audio.setAttribute('src', tracklist[i].path);
            totallengthFun();
            titleholder.innerHTML = tracklist[i].title;
            artistholder.innerHTML = tracklist[i].artist;
            audio.play()
            previousTrack = i;
        }
        if (audio.ended === true && shuffleOn === true) {
            i = Math.floor(Math.random() * tracklist.length);
            if (previousTrack != i) {
                songList[previousTrack].className = songList[previousTrack].className.slice(0, 8);
            }
            songList[i].className = songList[i].className + ' selected';
            audio.setAttribute('src', tracklist[i].path);
            totallengthFun();
            titleholder.innerHTML = tracklist[i].title;
            artistholder.innerHTML = tracklist[i].artist;
            audio.play()
            previousTrack = i;
        }
    };

    var playButtonClicked = function() {
        titleholder.innerHTML = tracklist[i].title;
        artistholder.innerHTML = tracklist[i].artist;
        var playListBox = document.querySelectorAll('.playlistbox>div');
        document.getElementsByClassName(playListBox[0].setAttribute('class', "onelist type2 standard1 selected"));

        songList[i].className = songList[i].className + ' selected';

        counter++;

        if (counter % 2 === 1) {
            playButton.setAttribute('style', 'background-image: url(style/images/pause.svg);');
            interval = setInterval(remaintimeCalculator, 1000);
            audio.play();
        } else {
            playButton.setAttribute('style', 'background-image: url(style/images/play.svg);');
            clearInterval(interval);
            audio.pause();
        }
        if (counter === 1) {
            remaintime.innerHTML = timeManagement(tracklist[i].duration);
        }
        totallengthFun();
    };

    var rewindClicked = function() {
        audio.playbackRate--;
    };

    var forwardClicked = function() {
        audio.playbackRate++;
    };

    var remaintimeCalculator = function() {
        seekbarInput.value = (audio.currentTime / tracklist[i].duration) * 100;
        seekbar();
        remaintimeFun();
        playNextTrack();
    };

    var remaintimeFun = function() {
        remaintime.innerHTML = timeManagement(tracklist[i].duration - Math.floor(audio.currentTime));
    };

    var seekbar = function () {
        if (seekbarInput.value >= 50) {
            seekbarInput.setAttribute('style', 'background: linear-gradient(to right, rgb(60, 210, 205) ' + seekbarInput.value + '%, rgb(220, 220, 220)' + (100-seekbarInput.value) + '%);');
        } else {
            seekbarInput.setAttribute('style', 'background: linear-gradient(to left, rgb(220, 220, 220) ' + (100-seekbarInput.value) + '%, rgb(60, 210, 205)' + seekbarInput.value + '%);');
        }
    };

    var timeManagement = function(fulltime) {
        if (fulltime > 60) {
            var minuteMan = Math.floor(fulltime / 60) + ':' + Math.floor(fulltime % 60);
            if (Math.floor(fulltime % 60)  < 10) {
                minuteMan = Math.floor(fulltime / 60) + ':0' + Math.floor(fulltime % 60);
            }
        } else {
            var minuteMan = Math.floor(fulltime);
        }
        return minuteMan
    };

    var totallengthFun = function() {
        totallength.innerHTML = timeManagement(tracklist[i].duration);
    };

    var shuffleClicked = function() {
        if (shuffleOn === false) {
            shuffleOn = true;
        } else {
            shuffleOn = false;
        }
    };

    var volumeClicked = function() {
        if (audio.muted === false) {
            audio.muted = true;
        } else {
            audio.muted = false;
        }
    };

    var volumebar = function () {
        audio.volume = volumebarInput.value / 100;

        if (volumebarInput.value >= 50) {
            volumebarInput.setAttribute('style', 'background: linear-gradient(to right, rgb(60, 210, 205) ' + volumebarInput.value + '%, rgb(220, 220, 220)' + (100-volumebarInput.value) + '%);');
        } else {
            volumebarInput.setAttribute('style', 'background: linear-gradient(to left, rgb(220, 220, 220) ' + (100-volumebarInput.value) + '%, rgb(60, 210, 205)' + volumebarInput.value + '%);');
        }
    };

    var seek = function () {
        audio.currentTime = seekbarInput.value / 100 * tracklist[i].duration;
    };

    playButton.addEventListener('click', playButtonClicked);
    rewind.addEventListener('click', rewindClicked);
    forward.addEventListener('click', forwardClicked);
    seekbarInput.onchange = seek;
    shuffle.addEventListener('click', shuffleClicked);
    volume.addEventListener('click', volumeClicked);
    volumebarInput.oninput = volumebar;
};

var favoriteButton = document.querySelector('.star');
favoriteButton.addEventListener('click', favoritePlus);

var getfavorite = function() {
    favoriteCall();
};

var getAllTrack = function() {
    trackCall();
};
getAllTrack();
