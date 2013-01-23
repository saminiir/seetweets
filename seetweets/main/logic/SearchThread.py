'''
Created on Jan 22, 2013

@author: sami
'''
from threading import Thread
import time
from seetweets.main.logic.TwitterPoller import TwitterPoller

class SearchThread(Thread):
    def __init__(self, tweetqueue):
        Thread.__init__(self)
        self.tweetqueue = tweetqueue
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        poller = TwitterPoller()
        
        while 1:
            json = poller.getTwitterSearchJson("suits")
            tweet = poller.getLatestTweet(json)
            self.tweetqueue.put(tweet)
            time.sleep(10) 
