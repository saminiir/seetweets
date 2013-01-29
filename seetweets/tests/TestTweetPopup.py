'''
Created on Jan 29, 2013

@author: sailniir
'''
from seetweets.main.Tweet import Tweet
from seetweets.main.gui.TweetPopup import TweetPopup
import unittest

class TestTweetPopup(unittest.TestCase):
    
    def testTextCutting(self):
        tweet = self.createTweet("")
        
        popup = TweetPopup(tweet)
        lines = popup.splitTextToLines(tweet.text, 20, 5)
        
        self.assertEqual(len(lines), 0)
        
        tweet = self.createTweet("test test test")
        lines = popup.splitTextToLines(tweet.text, 5, 5)
        self.assertEqual(len(lines), 3)
        
    def createTweet(self, text):
        return Tweet(tid=12345, hashtag="test", author="tester", time="12:00", text=text)