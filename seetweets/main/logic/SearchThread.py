'''
Created on Jan 22, 2013

Worker thread for querying tweets with Twitter API

@author: sailniir
'''
from threading import Thread
import time
from TwitterPoller import TwitterPoller
from ..Observable import Observable
import logging

class SearchThread(Thread, Observable):
    def __init__(self, tweetqueue, database):
        Thread.__init__(self)
        Observable.__init__(self)
        self.tweetqueue = tweetqueue
        self.database = database
        self.query = ""
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        poller = TwitterPoller()
        
        self.delay = 0
        waitTime = 0
        
        self.running = True
        
        while self.running:
            if not(self.isValid(self.query)) or self.interrupted: continue
            
            
            if self.delay > 0:
                self.notify("statusChanged", "Searching in " + str(self.delay) + " seconds..")
                self.delay -= 1
                time.sleep(1)
                waitTime = 0
                continue
            
            if self.isValid(self.query) and waitTime < 1:
                tid = self.getLatestTweetId(self.query)
                
                query = self.query
    
                self.notify("statusChanged", "Searching tweets..")
    
                try:
                    json = poller.getTwitterSearchJson(query, tid)
                    tweet = poller.getLatestTweet(json, query)
                except Exception as e:
                    self.notify("statusChanged", e.args[0])
                    self.interrupted = True
                    continue
                
                if tweet is not None:
                    logging.debug(tweet.text)
                    self.notify("statusChanged", "Found tweets! Showing..")
                    self.tweetqueue.put(tweet)
                    tweet.persist(self.database.getConnection())
                else:
                    self.notify("statusChanged", "No new tweets!")
                
                waitTime = 10
                
            if waitTime > 0:
                time.sleep(1)
                waitTime -= 1
                self.notify("statusChanged", "Searching again in " + str(waitTime) + "..")
                continue
                
            

    def getLatestTweetId(self, hashtag):
        '''
        Returns the latest tweet's id from db. If not found, returns zero.
        '''
        result = self.database.queryRows("SELECT MAX(tid) FROM tweets WHERE hashtag = ?", [hashtag])
        
        if result == None or result[0][0] == None:
            return 0
        
        return result[0][0]
    
    def isValid(self, hashtag):
        time.sleep(0.5)
        
        if len(hashtag) > 139:
            self.notify("statusChanged", "Too long query!")
            return False
        if len(hashtag) < 1:
            self.notify("statusChanged", "Give a query!")
            return False
        
        return True
    
    def setQuery(self, sender, event, msg):
        self.query = msg
        self.delay = 3
        self.interrupted = False
        
    def notify(self, events, msg=None):
        if self.running:
            self.notifyObservers(events, msg)
            
    def stop(self):
        self.running = False
        