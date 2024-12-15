from contextlib import nullcontext
from fileinput import close
from genericpath import isdir
import os
import os.path as path
from Log import Log

from data_struct import *
from auth import *


class DBE(Auth):
  
                
    def __init__(self, username, passkey, db_lock=None):

        self.TABLES=dict()
        self.DB_LOCK=db_lock
        Auth.__init__(self, username, passkey, self.DB_LOCK)
        """
        self.PRIVALAGES=None

        self.USERS=Table(table=os.path.join(os.path.curdir, 'users/')+'users.db')
        #self.USERS.addRow(username='cadet', passkey='pass123', privalages='None')Table(table='{}/{}'.format(db, table))
        self.USERS.updateRow(username='sdkjss', passw='ss76w')
        user_auth=self.Authenticate(username, passkey)
    
        if user_auth[0]:
            if db_lock is None:
                Log(Log.FAIL+'\nError: '+Log.ENDC+'Please specify a db to access.')
            else:
                if db_lock not in self.PRIVALAGES and 'ALL' not in self.PRIVALAGES:
                    Log(Log.FAIL+'Error: '+Log.ENDC+'You do not have privalages to access this database.')
                else:
                    Log(Log.OKBLUE+'Authentication Successfull'+Log.ENDC)
                    self.loadTables()
                    print(self.TABLES)
                #print(self.PRIVALAGES)
            
        else:
            Log(Log.FAIL+'Error:'+Log.ENDC+' Failed to authenticate, Please try again')
        """
    
    """
    def Authenticate(self, username, password):

        for row in self.USERS.rows[1:]:
            if row['username']==username and row['passkey']==password:
                self.PRIVALAGES=eval(row['privalages'])
                return (True, username)
            
        return False
    """

    def loadTables(self):
        db=os.path.join(os.path.curdir, self.DB_LOCK)
        
        for table in os.listdir(db):
            tb='{}/{}'.format(db, table)
            self.TABLES.update({table:Table(table=tb)})
        

    def createTable(self, table, col_names={}, rows=[]):
        tbs=os.listdir(self.DB_LOCK)
        tb=table=table+'.db'
        
        tb_data=[col_names, rows]
    
        if tb not in tbs:
            self.TABLES.update({table: Table(new_tb=True, tb_data=tb_data, table=self.DB_LOCK+'/'+tb)})
        else:
            Log(Log.FAIL+'Error: '+Log.ENDC+' table already exists, choose another table name')
    

    def createDB(self, db_name):
        if not os.path.isdir(db_name):
            os.mkdir(db_name)
            Log(Log.OKBLUE+'{} created successfully'.format(db_name)+Log.ENDC)

        else:
            Log(Log.FAIL+'Error: Database already exists!'+Log.ENDC)
    
    def grantPrivalages(self, user, privalages):
        pass

    def commit(self):
        cont=''

        for table in self.TABLES:  
            col_names='#'.join(map(lambda x: '{}{};{}{}'.format('{', x.data, [x.type, x.limit, x.null], '}'), table.rows[0]))
            cont+=col_names            
            for row in table.rows[1:]:
                cont+='\n{}'.format('#'.join(v for k,v in row.items()))
            
            tb=open(table.path, 'w')
            tb.write(cont)
            tb.close()
        
        return 1 

    def delDB(self, db_name):
        if path.isdir(db_name):
            os.rmdir(db_name)
            return 'DB ({}) deleted.'.format(db_name)
        else:
            return 'Failed to delete {}. Databse does not exist'.format(db_name)

db=DBE('root', 'secret0112', 'mock')
