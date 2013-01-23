'''
Created on Jan 23, 2013

Class representing a popup showing the tweet message 

@author: sailniir
'''
from Tkinter import Toplevel, Canvas
from threading import Timer

class TweetPopup(Toplevel):
    
    def __init__(self, tweet):
        Toplevel.__init__(self)
        self.tweet = tweet
        
        self.wm_overrideredirect(True)
        canvas = Canvas(self, width=100, height=100)
        canvas.pack()
        canvas.create_text(10, 10, text=tweet.text)

