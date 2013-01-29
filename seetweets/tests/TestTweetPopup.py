'''
Created on Jan 29, 2013

@author: sailniir
'''
from seetweets.main.Tweet import Tweet
from seetweets.main.gui.TweetPopup import TweetPopup
import unittest

class TestTweetPopup(unittest.TestCase):
    
    def testTextCutting(self):
        lines = self.cutText(text="", lastindex=0, threshold=0)
        self.assertEqual(len(lines), 0)
        
        lines = self.cutText("test test test", 5, 5)
        self.assertEqual(len(lines), 3)
        
        lines = self.cutText("xxxxxxx", 5, 5)
        self.assertEqual(len(lines), 2)
        
        lines = self.cutText("xxx", 5, 5)
        self.assertEqual(len(lines), 1)
        
        lines = self.cutText("tst tst tst tst tst tst", 4, 1)
        self.assertEqual(len(lines), 6)
        
        
    def cutText(self, text, lastindex, threshold):
        tweet = self.createTweet(text)
        popup = TweetPopup(tweet)
        lines = popup.splitTextToLines(tweet.text, lastindex=lastindex, threshold=threshold)
        
        return lines
        
    def createTweet(self, text):
        return Tweet(tid=12345, hashtag="test", author="tester", time="12:00", text=text)