'''
Created on Jan 22, 2013

@author: sami
'''
import unittest
from seetweets.main.logic.TwitterPoller import TwitterPoller

class TestTwitterPolling(unittest.TestCase):
    
    def testTwitterSearch(self):
        twitterPoller = TwitterPoller()
        
        self.assertRaises(TypeError, twitterPoller.searchTwitter(""))
        
        