'''
Created on Jan 22, 2013

@author: sami
'''
from Tkinter import Entry, StringVar
from seetweets.main.Observable import Observable

class HashInput(Entry, Observable):
    
    def __init__(self, master=None):
        Observable.__init__(self)
        hashText = StringVar()
        
        hashText.trace("w", lambda nm, idx, mode, var=hashText: self.textChanged(hashText))

        Entry.__init__(self, master, textvariable = hashText)
        
    def textChanged(self, sv):
        self.notifyObservers('hashChanged', sv.get())
        print sv.get()