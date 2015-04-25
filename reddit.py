# import modules
import requests
import json
import time

# get the feed
print "Please enter the subreddit you'd like to list."
subreddit = raw_input("> ")
print

print "Top 25 Posts in /r/%s:" % subreddit

url = "http://www.reddit.com/r/%s/hot/.json" % subreddit
headers = { 'User-Agent' : "API Testing Project 0.1"}

r = requests.get(url, headers=headers)
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)

# Loop through the result.
for item in data['data']['children']:

    print "-------------------------------------------"
    print "Title: %s" % (item['data']['title'])
    print "Author: %s" % (item['data']['author'])
    print "UpVotes: %i" % (item['data']['ups'])
    print "URL: %s" % (item['data']['url'])
    posted_epoch_time = int(item['data']['created'])
    posted_date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(posted_epoch_time))
    print "Posted: %s" % posted_date_time
