'''
Created on Jan 22, 2013

@author: sami
'''
from threading import Thread
import time

class SearchThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        self.searchTweets()
        
    def searchTweets(self):
        while 1:
            print "search thread test"
            time.sleep(5) 
