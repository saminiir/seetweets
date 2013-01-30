'''
Created on Jan 22, 2013

Main frame for the SeeTweets application. Handles the widgets

@author: sailniir
'''
from Tkinter import *
from HashInput import HashInput
import logging
import webbrowser

class MainFrame(Frame):
    
    def createWidgets(self):
        self.query = Label(self, text="Query:")
        self.query.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        self.hashentry = HashInput(self)
        self.hashentry['width'] = 20
        self.hashentry.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        
        self.statuslabel = Label(self, anchor=W)
        self.statuslabel["text"] = "Give a hashtag!"
        self.statuslabel.grid(row=1, column=0, sticky=W, columnspan=2, padx=5, pady=5)
        
        self.createMenus()
        
    def __init__(self, title, master=None):
        Frame.__init__(self, master, width=200, height=200)
        self.master.title(title)
        self.pack()
        self.createWidgets()
        
    def createMenus(self):
        menubar = Menu(self.master, tearoff=0, bd=1)
        self.master.config(menu=menubar)
        
        filemenu = Menu(menubar, tearoff=0)
        #filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="Twitter Search API", command=lambda url="https://dev.twitter.com/docs/using-search":self.openBrowser(url))
        helpMenu.add_command(label="About", command=self.showAboutMenu)
        menubar.add_cascade(label="Help", menu=helpMenu)
        
    def addObserverToHashEntry(self, observer, events=None):
        '''
        TODO: needs refactoring
        '''
        self.hashentry.addObserver(observer, events)
        
    def statusChanged(self, sender, event, msg):
        if event == "statusChanged":
            self.statuslabel["text"] = msg
            logging.debug("msg: " + msg)
        
    def handleException(self, sender, event, msg):
        if event == "exception":
            self.showException(msg)
            
    def showException(self, msg):
        logging.debug("msg: " + str(msg.args))
        
    def showAboutMenu(self):
        top = Toplevel(height=500)
        top.title("About SeeTweets")

        
        msg = Message(top, text="SeeTweets is an application for displaying Twitter-tweets with the given criteria.\n\nUses Twitter's Search API.\n\nMade by Sami Niiranen")
        msg['pady'] = 20
        msg.pack()
        
        button = Button(top, text="Close", command=top.destroy)

        button.pack()
        
        top['height'] = 500
        top['width'] = 400
        top['pady'] = 10
        top['padx'] = 20
    
    def openBrowser(self, url):
        webbrowser.open(url)
        
