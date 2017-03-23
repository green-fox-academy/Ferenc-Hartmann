# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crutial component, find out what it is and insert it too!

url = "https//www.reddit.com/r/nevertellmethebots"

url = (url[0:5] + ":" + url[6:])
url = (url[0:38] + "odds")

print(url)
