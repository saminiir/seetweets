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
        self.wm_attributes("-topmost", 1)
        self.tweet = tweet
        self.wm_overrideredirect(True)
        self.lines = []
        
        self.width = 300
        self.height = 48
        
        lines = self.splitTextToLines(tweet.text, lastindex = 40, threshold = 8)
        self.addLinesToHeight(lines)
        
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, 200, 200))
        canvas = Canvas(self, borderwidth=0, relief="sunken")
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
            canvas.create_text(10, y, text=line.strip(), anchor=NW)
            y += linespace

    def splitTextToLines(self, text, lastindex, threshold):
        '''
        Splits the tweet text for changing popup size 
        TODO: The tweetpopup probably shouldn't "know" this functionality
        '''
        
        lines = []
        
        #Algorithm for splitting text into lines. Finds the nearest
        #whitespace of the given index and cuts that line to list.
        #Optional threshold variable, that forces cut if no whitespace
        #found in given amount of traversal (threshold)
        while len(text) > 0:
            if (len(text) <= lastindex):
                lines.append(text)
                break
            
            left = lastindex
            right = lastindex
            
            #TODO: Refactor!
            for i in range(threshold):
                if left >= 0 and text[left] == ' ':
                    text = self.appendLineAndReturnTrailing(lines, left, text)
                    break
                elif right < len(text) and text[right] == ' ':
                    text = self.appendLineAndReturnTrailing(lines, right, text)
                    break
                 
                #If we got here on the last round, force line cut
                if i + 1 == threshold:
                    text = self.appendLineAndReturnTrailing(lines, lastindex, text)
                    
                left -= 1
                right += 1
                
        return lines
    
    def appendLineAndReturnTrailing(self, lines, index, text):
        lines.append(text[:index])
        return text[index:]
    
    def addLinesToHeight(self, lines):
        for i in range(len(lines)):
            self.height += 15
