'''
Created on Jan 22, 2013

@author: sami
'''
import urllib
import json
from seetweets.main.Tweet import Tweet
from urllib import urlencode

class TwitterPoller():
    
    def __init__(self):
        print ""
        
    def getTwitterSearchJson(self, hashtag, sinceid = 0):
        if len(hashtag) < 2: raise Exception("Hashtag was too short!")
        
        getcommand = urlencode("http://search.twitter.com/search.json?since_id=" + str(sinceid) + "&q=%40" + hashtag)
        
        f = urllib.urlopen(getcommand).read()
        result = json.loads(f)
        
        return result
        
    #===========================================================================
    # Returns a Tweet-object constructed from a given Twitter-Json 
    #===========================================================================
    def getLatestTweet(self, tweetsjson):
        results = tweetsjson['results']
        
        if len(results) < 1:
            return

        result = results[0]
        
        tid = result['id']
        time = result['created_at']
        author = result['from_user_name']
        text = result['text']

        tweet = Tweet(tid, time, author, text)
        
        tweet = Tweet(1225215, "20:57", "@Sami", "Testaan vaan etta toimiiko 1234556789 :)")
        
        return tweet