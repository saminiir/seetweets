'''
Created on Jan 22, 2013

Main frame for the SeeTweets application. Handles the widgets

@author: sailniir
'''
from Tkinter import *
from HashInput import HashInput

class MainFrame(Frame):
    
    def createWidgets(self):
        self.HASH = Label(self)
        self.HASH["text"] = "#"
        self.HASH.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        
        self.hashentry = HashInput(self)
        self.hashentry['width'] = 20
        self.hashentry.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        
        self.statuslabel = Label(self, anchor=W)
        self.statuslabel["text"] = "Give a hashtag!"
        self.statuslabel.grid(row=1, column=0, sticky=W, columnspan=2, padx=5, pady=5)
    
    def __init__(self, title, master=None):
        Frame.__init__(self, master, width=200, height=200)
        self.master.title(title)
        self.pack()
        self.createWidgets()
        
    def addObserverToHashEntry(self, observer, events=None):
        '''
        TODO: needs refactoring
        '''
        self.hashentry.addObserver(observer, events)
        
    def statusChanged(self, sender, event, msg):
        if event == "statusChanged":
            self.statuslabel["text"] = msg
            print "msg: " + msg
        
    def handleException(self, sender, event, msg):
        if event == "exception":
            self.showException(msg)
            
    def showException(self, msg):
        print "msg: " + str(msg.args)
        
