'''
Created on Jan 23, 2013

Class representing a popup showing the tweet message 

@author: sailniir
'''
from Tkinter import Toplevel, Canvas, PhotoImage
from Tkconstants import NW

class TweetPopup(Toplevel):
    
    def __init__(self, tweet):
        Toplevel.__init__(self)
        self.tweet = tweet
        self.wm_overrideredirect(True)
        self.lines = []
        
        lines = self.processText(tweet.text)
        
        self.width = 300
        self.height = 100
        
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, 100, 100))
        self.wm_attributes("-alpha", 0.7)
        canvas = Canvas(self, borderwidth=-1, relief="sunken")
        canvas.pack()
        
        self.createLayout(canvas)
        
        length = len(tweet.text)
        
        author = tweet.author
        canvas.create_text(80, 13, text="@" + author, fill="white")
        
        self.renderText(canvas, lines)
       # textpart1 = tweet.text[:length/2]
       # textpart2 = tweet.text[-length/2:]
        
       # canvas.create_text(100, 50, text=textpart1)
       # canvas.create_text(100, 75, text=textpart2)
        
#        canvas.create_image(100, 25, image=self.popupimg, tags="img")

    def createLayout(self, canvas):
        canvas.create_rectangle(0, 0, self.width, self.height, fill="white")
        canvas.create_rectangle(0, 0, self.width, 25, fill="black")
        self.twitterbird = PhotoImage(file="twitterbird2.gif")
        canvas.create_image(12.5, 12.5, image=self.twitterbird, tags="img")
    
    def renderText(self, canvas, lines):
        linespace = 25
        y = 35
        for line in lines:
            canvas.create_text(10, y, text=line, anchor=NW)
            y += linespace

    def processText(self, text):
        '''
        Splits the tweet text for changing popup size 
        '''
        
        textlength = len(text)
        
        linecount = textlength / 25
        
        print "text length: " + str(textlength) + ", linecount: " + str(linecount)
        
        lines = []
        
        j = 0
        
        threshold = 40
        linecount = textlength / threshold
        
        for i in range(linecount):
            end = (i+1)*threshold
            
            if end > textlength:
                end = textlength
            
            line = text[i*threshold:end]
            lines.append(line)
            
        
        #for i in range(textlength):
       #     if j > threshold and text[i] == ' ':
        #        lines.append(text[i-j:j])
       #         j = 0
       #     print text[i]
       #     j += 1
            
        #if len(lines) < 1:
       #     lines = [text]
        print lines
        
        return lines
