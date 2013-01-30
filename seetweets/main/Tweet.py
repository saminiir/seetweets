'''
Created on Jan 23, 2013

A class representing a single tweet.

@author: sailniir
'''

class Tweet():
    
    def __init__(self, tid, query, time, author, text):
        self.tid = tid
        self.query = query
        self.time = time
        self.author = author
        self.text = text
        
    def persist(self, connection):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tweets VALUES (?, ?, ?, ?, ?)", [self.tid, self.query, self.time, self.author, self.text])
        connection.commit()
        connection.close()
