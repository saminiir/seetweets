'''
Created on Jan 22, 2013

@author: sailniir
'''
from Tkinter import *
from seetweets.main.gui.HashInput import HashInput

class MainFrame(Frame):
    
    def createWidgets(self):
        self.HASH = Label(self)
        self.HASH["text"] = "#"
        self.HASH.pack(side = LEFT)
        
        self.hashentry = HashInput(self)
        self.hashentry['width'] = 20
        self.hashentry.pack(side = LEFT)
    
    def __init__(self, title, master=None):
        Frame.__init__(self, master, width=200, height=200)
        #self['bg'] = 'red'
        self.master.title(title)
        self.pack()
        self.createWidgets()
        
    def addObserverToHashEntry(self, observer, events=None):
        '''
        TODO: needs refactoring
        '''
        self.hashentry.addObserver(observer, events)
        
