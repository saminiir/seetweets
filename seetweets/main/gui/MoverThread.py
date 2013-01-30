'''
Created on Jan 27, 2013

A custom thread for moving a widget on the screen.
Currently only knows how to slide the element in to view from the right.

@author: sailniir
'''
from threading import Thread, Timer
import time

class MoverThread(Thread):
    
    def __init__(self, element, seconds):
        Thread.__init__(self)
        self.element = element
        self.seconds = seconds
        
    def run(self):
        '''
        The main threaded algorithm for moving the GUI-element
        '''
        self.running = True
        
        x = self.element.winfo_screenwidth()
        
        #These values could be read from a config file or preferences menu
        y = 250
        
        width = self.element.width
        height = self.element.height
        
        border = x - width
        
        timer = Timer(self.seconds, self.stop)
        timer.start()
        
        tick = 0
        
        while self.running:
            tick += 1
            self.element.geometry("%dx%d+%d+%d" % (width, height, x, y))
            
            if (x > border):
                x -= 3
            
            time.sleep(0.01)
        
        self.element.destroy()
            
    def stop(self):
        self.running = False