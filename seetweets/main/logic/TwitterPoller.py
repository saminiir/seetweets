'''
Created on Jan 22, 2013

@author: sami
'''
import urllib
import json

class TwitterPoller():
    
    def __init__(self):
        print ""
        
    def searchTwitter(self, hashtag):
        f = urllib.urlopen("http://search.twitter.com/search.json?q=%40" + hashtag).read()
        test = json.loads(f)
        
        print test
        
        return "lol"
        
    def getLatestTweet(self, tweets):
        print "lol"