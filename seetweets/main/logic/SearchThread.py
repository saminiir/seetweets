'''
Created on Jan 22, 2013

@author: sami
'''
from threading import Thread
import time
from seetweets.main.logic.TwitterPoller import TwitterPoller

class SearchThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        poller = TwitterPoller()
        
        while 1:
            json = poller.getTwitterSearchJson("suits")
            poller.getLatestTweet(json)
            time.sleep(10) 
