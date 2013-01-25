'''
Created on Jan 25, 2013

Class representing a sender. Implements the Observer-pattern.

@author: sailniir
'''
import types

class Observable():
    
    def __init__(self):
        self.observers = {}
        
    def addObserver(self, observer, events=None):
        '''
        Adds an observer to the sender, with optional event-types
        '''
        if events is not None and type(events) not in (types.TupleType, types.ListType):
            events = (events,)
            
        self.observers[observer] = events
    
    def notifyObservers(self, event=None, msg=None):
        '''
        Notifies all listeners attached to the observable
        '''
        
        for observer, events in self.observers.items():
            if events is None or event is None or event in events:
                observer(self, event, msg)
                
    def removeObserver(self, observer):
        del self.observers[observer]
                
        
             
