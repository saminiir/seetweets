'''
Created on Jan 24, 2013

Unit tests for database

@author: sailniir
'''
import unittest
from seetweets.main.database.Database import Database
from seetweets.main.Tweet import Tweet
class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.database = Database("test")
        
        self.initDb()
        
    def initDb(self):
        conn = self.database.getConnection();
        
        c = conn.cursor();
        
        c.execute('''DROP TABLE tweets''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS tweets
                    (tid INT, 
                    query TEXT, time TIMESTAMP, author TEXT, text TEXT)''')
        
        conn.commit()
        conn.close()
    
    def testSave(self):
        testTweet = Tweet(tid=12215, query="test", time="20:57", author="@Sami", text="test case test case test case")
        
        self.assertEquals(0, self.database.getCount("tweets"), "The database should be empty!")
        
        testTweet.persist(self.database.getConnection())
        
        self.assertEquals(1, self.database.getCount("tweets"), "The database should have exactly one row!")

        testTweet.persist(self.database.getConnection())
        
        self.assertEquals(2, self.database.getCount("tweets"), "The database should have exactly two rows!")