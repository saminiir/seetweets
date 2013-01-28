'''
Created on Jan 27, 2013

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
        self.running = True
        
        x = self.element.winfo_screenwidth()
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