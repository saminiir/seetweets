'''
Created on Jan 23, 2013

Class for controlling the SeeTweets-application. Handles the view and logic and delegates commands

@author: sailniir
'''
import os
import sys
#sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append("/home/sami/sami/code/seetweets/seetweets/main/")

from Queue import Queue
from logic.SearchThread import SearchThread
from Tkinter import *
from gui.MainFrame import MainFrame
from gui.TweetPopup import TweetPopup
from threading import Timer
from database.Database import Database
from gui.MoverThread import MoverThread
import sys

class Controller():
    
    def __init__(self):
        self.tweetqueue = Queue()
        self.database = Database()
        
    def invoke(self):
        '''
        Method for starting the controller
        '''
        
        self.searchThread = SearchThread(self.tweetqueue, self.database)
        self.mover = None
        
        self.root = Tk()
        self.root.resizable(FALSE,FALSE)
        
        self.root.after(5000, self.showNewTweetIfFound, self.root)
        
        seetweets = MainFrame("SeeTweets", self.root) 
        
        self.searchThread.addObserver(seetweets.handleException, events="exception")
        self.searchThread.addObserver(seetweets.statusChanged, events="statusChanged")
        
        #TODO: addObserverToElement ?
        seetweets.addObserverToHashEntry(self.searchThread.setHashtag, events="hashChanged")
        
        self.root.protocol("WM_DELETE_WINDOW", self.safelyExitApplication)
        
        self.searchThread.start()
        self.root.mainloop()
        
    def showNewTweetIfFound(self, root):
        '''
        Shows a new tweet as a popup, if found
        '''
        tweet = self.pollQueue()

        if tweet != None:
            self.showTweetFor(tweet, 8)

        #Lets call the function again in X milliseconds                
        root.after(5000, self.showNewTweetIfFound, root)
        
    def pollQueue(self):
        '''
        Method for polling the queue for tweets. Helps with thread-safety
        '''
        try:
            tweet = self.tweetqueue.get(block=False)
        except (Exception):
            return
        
        self.tweetqueue.task_done()
        
        return tweet
        
    def showTweetFor(self, tweet, seconds):
        '''
        Shows a tweet as a popup for given amount of seconds
        '''
        
        msg = TweetPopup(tweet)
        
        self.mover = MoverThread(msg, seconds).start()
        
        print "starting timer!"
        
    def safelyExitApplication(self):
        self.searchThread.stop()
        if not self.mover is None: self.mover.stop()
        self.root.destroy()
        #self.root.quit()
        print "Thanks for using SeeTweets!"
        sys.exit()
#        msg.geometry("%dx%d+%d+%d" % (300, 100, 300, 300))
        
    #    timer = Timer(seconds, mover.stop)
     #   timer.start()
        
