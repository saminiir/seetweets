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
        
        self.width = 300
        self.height = 48
        
        lines = self.processText(tweet.text)
        

        
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, 100, 100))
        self.wm_attributes("-alpha", 0.7)
        canvas = Canvas(self, borderwidth=-1, relief="sunken")
        canvas.pack()
        
        self.createLayout(canvas)
        
        author = tweet.author
        canvas.create_text(30, 6, text="@" + author, fill="white", anchor=NW)
        
        self.renderText(canvas, lines)

    def createLayout(self, canvas):
        canvas.create_rectangle(0, 0, self.width, self.height, fill="white")
        canvas.create_rectangle(0, 0, self.width, 25, fill="black")
        self.twitterbird = PhotoImage(file="twitterbird.gif")
        canvas.create_image(12.5, 12.5, image=self.twitterbird, tags="img")
    
    def renderText(self, canvas, lines):
        linespace = 17
        y = 35
        for line in lines:
            canvas.create_text(10, y, text=line, anchor=NW)
            y += linespace

    def processText(self, text):
        '''
        Splits the tweet text for changing popup size 
        '''
        
        textlength = len(text)
        
        lines = []
        
        j = 0
        
        threshold = 40
        linecount = textlength / threshold
        
        for i in range(linecount+1):
            end = (i+1)*threshold
            
            if end > textlength:
                end = textlength
            
            line = text[i*threshold:end]
            lines.append(line)
            self.height += 15
            
        
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
