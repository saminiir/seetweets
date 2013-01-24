'''
Created on Jan 23, 2013

Class representing a popup showing the tweet message 

@author: sailniir
'''
from Tkinter import Toplevel, Canvas, PhotoImage

class TweetPopup(Toplevel):
    
    def __init__(self, tweet):
        Toplevel.__init__(self)
        self.tweet = tweet
        self.wm_overrideredirect(True)
        self.lines = []
        
        self.process(tweet)
        
        self.geometry("%dx%d+%d+%d" % (300, 100, 100, 100))
        self.wm_attributes("-alpha", 0.7)
        canvas = Canvas(self, borderwidth=-1, relief="sunken")
        canvas.pack()

        length = len(tweet.text)
        print len(tweet.text)
        
        textpart1 = tweet.text[:length/2]
        textpart2 = tweet.text[-length/2:]
        
        canvas.create_text(100, 25, text=textpart1)
        canvas.create_text(100, 50, text=textpart2)
        self.popupimg = PhotoImage(file="tweetpopup2.gif")
#        canvas.create_image(100, 25, image=self.popupimg, tags="img")

    def process(self, tweet):
        textlength = len(tweet.text)
        
        linecount = textlength / 25
        print linecount
        
        self.lines = []
        
        for i in range(linecount):
            print i
            i = i+25