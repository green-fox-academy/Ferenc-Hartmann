'use strict';
// Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
// Also, the URL is missing a crutial component, find out what it is and insert it too!

var url = "https//www.reddit.com/r/nevertellmethebots";

console.log(url);

var url1 = url.replace(/https/, 'https:');
var url2 = url1.replace(/bots/, 'odds');
url = url2;
console.log(url);
