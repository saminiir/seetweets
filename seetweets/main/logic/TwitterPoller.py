'''
Created on Jan 22, 2013

Class for accessing the Twitter API

@author: sailniir
'''
import urllib
import json
from ..Tweet import Tweet
from urllib import quote_plus, urlencode
import logging

class TwitterPoller():
    
    def __init__(self):
        print ""
        
    def getTwitterSearchJson(self, hashtag, sinceid = 0):
        if len(hashtag) < 2: raise Exception("Hashtag was too short!")
        
        params = urlencode({'since_id' : sinceid, 'q' : hashtag})
        #TODO: url encoding!
        getcommand = "http://search.twitter.com/search.json?%s" % params
        
        print getcommand
        
        f = urllib.urlopen(getcommand).read()
        result = json.loads(f)
        
        if "error" in result:
            raise Exception(result['error'])
        
        if "results" in result:
            if sinceid == 0 and len(result['results']) < 1:
                raise Exception("No tweets with this hashtag!")
        
        return result
        
    def getLatestTweet(self, tweetsjson, hashtag):
        '''
        Returns a Tweet-object constructed from a given Twitter-Json 
        '''
        
        results = tweetsjson['results']
        
        logging.info(results)
        
        if len(results) < 1:
            return None

        result = results[0]
        
        tid = result['id']
        time = result['created_at']
        author = result['from_user_name']
        text = result['text']

        tweet = Tweet(tid, hashtag, time, author, text)
        
        return tweet