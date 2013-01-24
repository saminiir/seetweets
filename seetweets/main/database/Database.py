'''
Created on Jan 23, 2013

@author: sami
'''
import sqlite3
class Database():
    
    def __init__(self, name="tweets"):
        self.name = name
        self.initTables()
    
    def getConnection(self):
        return sqlite3.connect(self.name + '.db')

    def initTables(self):
        conn = self.getConnection()
        
        c = conn.cursor()
        
        #c.execute('''DROP TABLE tweets''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS tweets
                    (tid INT, 
                    hashtag TEXT, time TIMESTAMP, author TEXT, text TEXT)''')
        
        conn.commit()
        conn.close()
        
    def getCount(self, tablename):
        conn = self.getConnection()
        
        c = conn.cursor()
        
        c.execute("SELECT COUNT(*) FROM " + (tablename))
        conn.commit()
        
        return c.fetchone()[0]
        