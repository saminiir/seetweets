'''
Created on Jan 23, 2013

@author: sailniir
'''
from Queue import Queue
from seetweets.main.logic.SearchThread import SearchThread
from Tkinter import *
from seetweets.main.gui.MainFrame import MainFrame
from seetweets.main.gui.TweetPopup import TweetPopup
from threading import Timer
from seetweets.main.database.Database import Database

class Controller():
    
    def __init__(self):
        self.tweetqueue = Queue()
        self.database = Database()
        
    def invoke(self):
        searchThread = SearchThread(self.tweetqueue, self.database)
        searchThread.start()
        
        root = Tk()
        root.resizable(FALSE,FALSE)
        
        root.after(5000, self.pollQueue, root)
        seetweets = MainFrame("SeeTweets", root) 
        root.mainloop()
        
    def pollQueue(self, root):
        tweet = self.tweetqueue.get()
        print "text " + tweet.text
        msg = TweetPopup(tweet)
        
        timer = Timer(2, msg.destroy)
        timer.start()
        
        self.tweetqueue.task_done()
        root.after(5000, self.pollQueue, root)
