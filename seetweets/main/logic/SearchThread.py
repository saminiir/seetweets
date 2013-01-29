'''
Created on Jan 22, 2013

Worker thread for querying tweets with Twitter API

@author: sailniir
'''
from threading import Thread
import time
from TwitterPoller import TwitterPoller
from ..Observable import Observable

class SearchThread(Thread, Observable):
    def __init__(self, tweetqueue, database):
        Thread.__init__(self)
        Observable.__init__(self)
        self.tweetqueue = tweetqueue
        self.database = database
        self.hashtag = ""
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        poller = TwitterPoller()
        
        self.delay = 0
        
        self.running = True
        
        while self.running:
            if not(self.isValid(self.hashtag)) or self.interrupted: continue
            
            if self.delay > 0:
                self.notifyObservers("statusChanged", "Searching in " + str(self.delay) + " seconds..")
                self.delay -= 1
                time.sleep(1)
                continue
            
            if self.isValid(self.hashtag):
                tid = self.getLatestTweetId(self.hashtag)
                
                hashtag = self.hashtag
    
                self.notifyObservers("statusChanged", "Searching tweets..")
    
                try:
                    json = poller.getTwitterSearchJson(hashtag, tid)
                    tweet = poller.getLatestTweet(json, hashtag)
                except Exception as e:
                    self.notifyObservers("statusChanged", e.args[0])
                    self.interrupted = True
                    continue
                    
                self.notifyObservers("statusChanged", "Found tweets! Showing..")
                self.tweetqueue.put(tweet)
                tweet.persist(self.database.getConnection())
                
            time.sleep(10)

    def getLatestTweetId(self, hashtag):
        result = self.database.queryRows("SELECT MAX(tid) FROM tweets WHERE hashtag = ?", [hashtag])
        
        if result == None or result[0][0] == None:
            return 0
        
        return result[0][0]
    
    def isValid(self, hashtag):
        time.sleep(0.5)
        
        if len(hashtag) > 139:
            self.notifyObservers("statusChanged", "Too long hashtag!")
            return False
        if len(hashtag) < 1:
            self.notifyObservers("statusChanged", "Give a hashtag!")
            return False
        
        return True
    
    def setHashtag(self, sender, event, msg):
        if event == "hashChanged":
            self.hashtag = msg
            self.delay = 3
            self.interrupted = False
            
    def stop(self):
        self.running = False
        