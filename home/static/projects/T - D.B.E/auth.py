from data_struct import *
import os
from Log import Log

class Auth():

    def __init__(self, username, passkey, db_lock):

        self.PRIVALAGES=None #variable to store user privalages

        self.USERS=Table(table=os.path.join(os.path.curdir, 'users/')+'users.db') #table of registered users
     
        user_auth=self.Authenticate(username, passkey)

        #check authentication status and privalages
        if user_auth[0]:
            if db_lock is None:
                Log(Log.FAIL+'\nError: '+Log.ENDC+'Please specify a db to access.')
            else:
                if db_lock not in self.PRIVALAGES and 'ALL' not in self.PRIVALAGES:
                    Log(Log.FAIL+'Error: '+Log.ENDC+'You do not have privalages to access this database.')
                else:
                    self.loadTables()
                #print(self.PRIVALAGES)
            
        else:
            Log(Log.FAIL+'Error:'+Log.ENDC+' Failed to authenticate, Please try again')
        
    
    #User authentication function 
    def Authenticate(self, username, password):

        for row in self.USERS.rows[1:]:
            if row['username']==username and row['passkey']==password:
                self.PRIVALAGES=eval(row['privalages'])
                Log(Log.OKGREEN+"Authentication successful. "+Log.ENDC+" (User: {}) \n".format(username))
                return (True, username)
            
        Log(Log.WARNING+"Authentication successful."+Log.ENDC)
        return False