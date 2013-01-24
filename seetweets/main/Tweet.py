'''
Created on Jan 23, 2013

A class representing a single tweet.
Knows the time, author and content of a tweet

@author: sami
'''

class Tweet():
    
    def __init__(self, tid, time, author, text):
        self.tid = tid
        self.time = time
        self.author = author
        self.text = text
        
    def persist(self):
        raise NotImplementedError