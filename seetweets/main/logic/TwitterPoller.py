'''
Created on Jan 22, 2013

@author: sami
'''
import urllib
import json
from seetweets.main.Tweet import Tweet
from urllib import quote_plus

class TwitterPoller():
    
    def __init__(self):
        print ""
        
    def getTwitterSearchJson(self, hashtag, sinceid = 0):
        if len(hashtag) < 2: raise Exception("Hashtag was too short!")
        
        getcommand = "http://search.twitter.com/search.json?since_id=" + str(sinceid) + "&q=%40" + hashtag
        
        print getcommand
        
        f = urllib.urlopen(getcommand).read()
        result = json.loads(f)
        
        return result
        
    def getLatestTweet(self, tweetsjson, hashtag):
        '''
        Returns a Tweet-object constructed from a given Twitter-Json 
        '''
        
        results = tweetsjson['results']
        
        if len(results) < 1:
            return

        result = results[0]
        
        print results
        
        tid = result['id']
        time = result['created_at']
        author = result['from_user_name']
        text = result['text']

        tweet = Tweet(tid, hashtag, time, author, text)
        
        return tweet