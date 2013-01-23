'''
Created on Jan 22, 2013

@author: sami
'''
from seetweets.main.gui.MainFrame import MainFrame 
from Tkinter import *
from threading import Timer
from seetweets.main.logic.SearchThread import SearchThread

def hello():
    print "hello, world"
#guiThread = GUIThread()
#guiThread.start()

searchThread = SearchThread()
searchThread.start()

t = Timer(1.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed


root = Tk()
root.resizable(FALSE,FALSE)
#root.overrideredirect(TRUE)
seetweets = MainFrame("SeeTweets", root) 
root.mainloop()




