'''
Created on Jan 22, 2013

Custom component for the hash input field

@author: sailniir
'''
from Tkinter import Entry, StringVar
from ..Observable import Observable

class HashInput(Entry, Observable):
    
    def __init__(self, master=None):
        Observable.__init__(self)
        hashText = StringVar()
        
        hashText.trace("w", lambda nm, idx, mode, var=hashText: self.textChanged(hashText))

        Entry.__init__(self, master, textvariable = hashText)
        
    def textChanged(self, sv):
        '''
        Raises a text changed -event
        ''' 
        self.notifyObservers('queryChanged', sv.get())