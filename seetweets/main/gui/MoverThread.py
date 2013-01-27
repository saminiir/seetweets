'''
Created on Jan 27, 2013

@author: sailniir
'''
from threading import Thread

class MoverThread(Thread):
    
    def __init__(self, element, seconds):
        Thread.__init__(self)
        self.element = element
        print "mover"
        
    def run(self):
        self.running = True
        
        x = 100
        y = 100
        
        while self.running:
            print "moving"
            self.element.geometry("%dx%d+%d+%d" % (300, 100, x, y))
            x += 0.2
            
            
    def stop(self):
        self.running = False