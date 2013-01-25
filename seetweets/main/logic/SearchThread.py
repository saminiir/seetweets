'''
Created on Jan 22, 2013

@author: sami
'''
from threading import Thread
import time
from seetweets.main.logic.TwitterPoller import TwitterPoller
from seetweets.main.Tweet import Tweet

class SearchThread(Thread):
    def __init__(self, tweetqueue, database):
        Thread.__init__(self)
        self.tweetqueue = tweetqueue
        self.database = database
        self.hashtag = ""
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        poller = TwitterPoller()
        
        while 1:
            if len(self.hashtag) > 0:
                print self.hashtag
                
                tid = self.getLatestTweetId(self.hashtag)
                
                print tid
    
                hashtag = self.hashtag
    
                print "hashtag is: " + hashtag
    
                json = poller.getTwitterSearchJson(hashtag, tid)
                tweet = poller.getLatestTweet(json, hashtag)
                
                if tweet != None:
                    self.tweetqueue.put(tweet)
                    tweet.persist(self.database.getConnection())
    
    #            self.database.dropTable("tweets")
    #            self.database.initTables()
    
               # tweet = Tweet(tid=1225215, hashtag="suits", time="20:57", author="@Sami", text="Testaan vaan etta toimiiko 1234556789 :)")

            time.sleep(10) 



    def getLatestTweetId(self, hashtag):
        result = self.database.queryRows("SELECT MAX(tid) FROM tweets WHERE hashtag = ?", [hashtag])
        
        if result == None or result[0][0] == None:
            return 0
        
        return result[0][0]

    def setHashtag(self, sender, event, msg):
        if event == "hashChanged":
            self.hashtag = msg
        