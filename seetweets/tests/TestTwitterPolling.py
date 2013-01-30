'''
Created on Jan 22, 2013

@author: sailniir
'''
import unittest
from seetweets.main.logic.TwitterPoller import TwitterPoller
import json

class TestTwitterPolling(unittest.TestCase):
    
    def testTwitterSearch(self):
        twitterPoller = TwitterPoller()
        
        #self.assertRaises(Exception, twitterPoller.getTwitterSearchJson, "")
        
        #Tests will fail if e.g. Twitter goes down..Hmm!
      #  json = twitterPoller.getTwitterSearchJson("suits")
        
       # self.assertGreater(len(json), 10, "Json was too short!")
        
    def testGetLatestTweet(self):
        twitterPoller = TwitterPoller()
        
        queryinvalidJson = json.dumps({"error":"Invalid query"})
        
        result = twitterPoller.getLatestTweet(queryinvalidJson, "test")
        
        self.assertEquals(result, None, "There should be no Tweet returned!")
