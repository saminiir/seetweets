'''
Created on Jan 22, 2013

@author: sami
'''
from Tkinter import *
from seetweets.main.gui.HashInput import HashInput

class MainFrame(Frame):
    
    def createWidgets(self):
        self.HASH = Label(self)
        self.HASH["text"] = "#"
        self.HASH.pack(side = LEFT)
        
        hashentry = HashInput(self)
        hashentry['width'] = 20
        hashentry.pack(side = LEFT)
    
    def __init__(self, title, master=None):
        Frame.__init__(self, master, width=200, height=200)
        #self['bg'] = 'red'
        self.master.title(title)
        self.pack()
        self.createWidgets()
