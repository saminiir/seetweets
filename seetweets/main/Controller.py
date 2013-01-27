'''
Created on Jan 23, 2013

Class for controlling the SeeTweets-application. Handles the view and logic and delegates commands

@author: sailniir
'''
from Queue import Queue
from seetweets.main.logic.SearchThread import SearchThread
from Tkinter import *
from seetweets.main.gui.MainFrame import MainFrame
from seetweets.main.gui.TweetPopup import TweetPopup
from threading import Timer
from seetweets.main.database.Database import Database
from seetweets.main.gui.MoverThread import MoverThread

class Controller():
    
    def __init__(self):
        self.tweetqueue = Queue()
        self.database = Database()
        
    def invoke(self):
        '''
        Method for starting the controller
        '''
        
        self.searchThread = SearchThread(self.tweetqueue, self.database)
        
        root = Tk()
        root.resizable(FALSE,FALSE)
        
        root.after(5000, self.showNewTweetIfFound, root)
        
        seetweets = MainFrame("SeeTweets", root) 
        
        self.searchThread.addObserver(seetweets.handleException, events="exception")
        self.searchThread.addObserver(seetweets.statusChanged, events="statusChanged")
        
        #TODO: addObserverToElement ?
        seetweets.addObserverToHashEntry(self.searchThread.setHashtag, events="hashChanged")
        
        self.searchThread.start()
        root.mainloop()
        
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
        
        mover = MoverThread(msg, seconds).start()
        
        print "starting timer!"
#        msg.geometry("%dx%d+%d+%d" % (300, 100, 300, 300))
        
    #    timer = Timer(seconds, mover.stop)
     #   timer.start()
        
