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
        self.database = database;
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        poller = TwitterPoller()
        
        while 1:
#            json = poller.getTwitterSearchJson("suits")
#            tweet = poller.getLatestTweet(testjson)
            tweet = Tweet(tid=1225215, hashtag="suits", time="20:57", author="@Sami", text="Testaan vaan etta toimiiko 1234556789 :)")
            self.tweetqueue.put(tweet)
            tweet.persist(self.database.getConnection())
            time.sleep(10) 
