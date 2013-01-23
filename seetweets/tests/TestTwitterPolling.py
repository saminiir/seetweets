'''
Created on Jan 22, 2013

@author: sami
'''
import unittest
from seetweets.main.logic.TwitterPoller import TwitterPoller

class TestTwitterPolling(unittest.TestCase):
    
    def testTwitterSearch(self):
        twitterPoller = TwitterPoller()
        
        self.assertRaises(Exception, twitterPoller.getTwitterSearchJson, "")
        
        #Tests will fail if e.g. Twitter goes down..Hmm!
        json = twitterPoller.getTwitterSearchJson("suits")
        
        self.assertGreater(len(json), 10, "Json was too short!")
        
    def testGetLatestTweet(self):
        twitterPoller = TwitterPoller()
        
        queryinvalidJson = '{"error":"Invalid query"}'
