'''
Created on Jan 22, 2013

Class for accessing the Twitter API

@author: sailniir
'''
import urllib
import json
from ..Tweet import Tweet
from urllib import urlencode
import logging

class TwitterPoller():
    
    def getTwitterSearchJson(self, query, sinceid = 0):
        '''
        Queries the Twitter Search API with given query.
        '''
        if len(query) < 2: raise Exception("Query was too short!")
        
        params = urlencode({'since_id' : sinceid, 'q' : query})
        getcommand = "http://search.twitter.com/search.json?%s" % params
        
        logging.debug(getcommand)
        
        f = urllib.urlopen(getcommand).read()
        result = json.loads(f)
        
        if "error" in result:
            raise Exception(result['error'])
        
        if "results" in result:
            if sinceid == 0 and len(result['results']) < 1:
                raise Exception("No tweets with this query!")
        
        return result
        
    def getLatestTweet(self, tweetsjson, query):
        '''
        Returns a Tweet-object constructed from a given Twitter-Json 
        '''
        
        if 'results' not in tweetsjson:
            return
        results = tweetsjson['results']
        
        logging.debug(results)
        
        if len(results) < 1:
            return None

        result = results[0]
        
        tid = result['id']
        time = result['created_at']
        author = result['from_user_name']
        text = result['text']
        
        logging.debug("TWEET TEXT: " + text)

        tweet = Tweet(tid, query, time, author, text)
        
        return tweet