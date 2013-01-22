'''
Created on Jan 22, 2013

@author: sami
'''
from Tkinter import Entry, StringVar

class HashInput(Entry):
    
    def __init__(self, master=None):
        hashText = StringVar()
        
        hashText.trace("w", lambda nm, idx, mode, var=hashText: self.textChanged(hashText))

        Entry.__init__(self, master, textvariable = hashText)
        
    def textChanged(self, sv):
        print sv.get()