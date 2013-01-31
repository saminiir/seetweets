'''
Created on Jan 23, 2013

Class representing the database operations

@author: sailniir
'''
import sqlite3
class Database():
    
    def __init__(self, name="tweets"):
        self.name = name
        self.initTables()
    
    def getConnection(self):
        return sqlite3.connect(self.name + '.db')

    def initTables(self):
        self.query('''CREATE TABLE IF NOT EXISTS tweets
                    (tid INT, 
                    query TEXT, time TIMESTAMP, author TEXT, text TEXT)''')
        
    def getCount(self, tablename):
        #SQL Inject warning! Can't use bindings with table names, so should at
        #least sanitize the input string
        result = self.queryRows("SELECT COUNT(*) FROM " + tablename)
        
        count = result[0][0]
        return count
        
    def query(self, statement):
        '''
        Executes an SQL-query against the database
        '''
        conn = self.getConnection()
        c = conn.cursor()
        
        c.execute(statement)
        conn.commit()
        
        conn.close()
        
    def queryRows(self, statement, params=None):
        '''
        Executes an SQL-query against the database and returns results
        '''
        conn = self.getConnection()
        c = conn.cursor()
        
        if (params == None):
            c.execute(statement)
        else:
            c.execute(statement, params)
            
        conn.commit()
        
        results = c.fetchall()
        
        conn.close()
        
        return results
    
    def dropTable(self, tablename):
        self.query("DROP TABLE " + tablename)
        