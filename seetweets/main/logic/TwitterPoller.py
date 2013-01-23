'''
Created on Jan 22, 2013

@author: sami
'''
import urllib
import json

class TwitterPoller():
    
    def __init__(self):
        print ""
        
    def getTwitterSearchJson(self, hashtag, sinceid = 0):
        if len(hashtag) < 2: raise Exception("Hashtag was too short!")
        
        getcommand = "http://search.twitter.com/search.json?since_id=" + str(sinceid) + "&q=%40" + hashtag
        
        f = urllib.urlopen(getcommand).read()
        result = json.loads(f)
        
        return result
        
    def getLatestTweet(self, tweetsjson):
        results = tweetsjson['results']
        
        print results[0]['text']