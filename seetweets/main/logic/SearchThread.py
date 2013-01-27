'''
Created on Jan 22, 2013

Worker thread for querying tweets with Twitter API

@author: sailniir
'''
from threading import Thread
import time
from seetweets.main.logic.TwitterPoller import TwitterPoller
from seetweets.main.Tweet import Tweet
from seetweets.main.Observable import Observable

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
        
        while 1:
            time.sleep(10) 
            
            if len(self.hashtag) > 0:
                tid = self.getLatestTweetId(self.hashtag)
                
                hashtag = self.hashtag
    
                self.notifyObservers("statusChanged", "Searching tweets..")
    
                try:
                    json = poller.getTwitterSearchJson(hashtag, tid)
                    tweet = poller.getLatestTweet(json, hashtag)
                except Exception as e:
                    self.notifyObservers("statusChanged", e.args[0])
                    continue
                    
                if tweet != None:
                    self.notifyObservers("statusChanged", "Found tweets!")
                    self.tweetqueue.put(tweet)
                    tweet.persist(self.database.getConnection())
            else:
                self.notifyObservers("statusChanged", "Give a hashtag!")

    def getLatestTweetId(self, hashtag):
        result = self.database.queryRows("SELECT MAX(tid) FROM tweets WHERE hashtag = ?", [hashtag])
        
        if result == None or result[0][0] == None:
            return 0
        
        return result[0][0]

    def setHashtag(self, sender, event, msg):
        if event == "hashChanged":
            self.hashtag = msg
        