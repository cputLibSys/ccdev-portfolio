from logging import exception
import random 
import sqlite3
from threading import activeCount
from Log import *
import time

class TransactionQueue():

    def __init__(self):

        self.arr = []

    def __str__(self) -> str:
        return str(self.arr)

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        return self.arr.pop(0)

    def front(self):
        return self.arr[0]

    def isEmpty(self):
        return self.arr==[]
    
    def size(self):
        return len(self.arr)

class Bank():
    db_conn=None
    accounts=dict()
    _transactions = TransactionQueue()
    __suspectTransactions=[]

    def __init__(self):
        self.accounts=None
      

    def connectDB(self, db):
        Log('\n'+Log.OKBLUE+'OK -> '+Log.ENDC+'Bank DB Connected\n')
        self.db_conn=sqlite3.connect(db)        
        self.accounts=self.__getAccounts()
        Log(Log.OKCYAN+'All accounts loadded successfully.'+Log.ENDC)

    def createAccount(self, name, balance, int_rate, pin):
        self.__createAccount( name, balance, int_rate, pin)

    def __createAccount(self, name, balance, int_rate, pin):
        try:

            def genAccNo():

                id = str(random.randrange(100, 999))+chr(random.randrange(65, 90))+chr(random.randrange(65, 90))+str(random.randrange(10, 99))+chr(random.randrange(65, 90))
            
                if id in self.accounts:
                
                    return self.genTransID()

                return id

            acc_no=genAccNo()

            self.db_conn.execute('''INSERT INTO accounts (account_no, name, balance, int_rate, pin) VALUES (?, ?, ?, ?, ?);''', 
            (
                acc_no, name, balance, int_rate, pin
            ))
            self.db_conn.commit()
            print('Account ({}) created for {}'.format(acc_no, name), '\n')
            print(self.__getAccounts())

        except Exception as e:
            print('\n', e, '\n')

    def __getAccounts(self):
        accs={}
        def convToDict(arr):
            acc={
                arr[0]:{
                'name': arr[1],
                'balance': arr[2],
                'int_rate': arr[3],
                'pin': arr[4]
                }
            }
            return acc

        acc_s=map(convToDict, list(self.db_conn.execute('SELECT * FROM accounts;')))
        for acc in acc_s:
            accs.update(acc)

        return accs

    def VerifyTransactions(self):
        self.__veifyTransactions()

    def __veifyTransactions(self):
        import time 
        while not self._transactions.isEmpty():
            if self._transactions.front()['amount']>10000:
                self.__suspectTransactions.append(self._transactions.front())
            
            Log(Log.OKCYAN+'Processing ->'+Log.ENDC, self._transactions.front(),'\n')
            transaction= self._transactions.dequeue()
            self.db_conn.execute('INSERT INTO (t_id, rec_acc_no, orig_acc_no, _to, amount, time_stamp) VALUES (?, ?, ?, ?, ?, ?)', (
                transaction.t_id,transaction.rec_acc_no,transaction.orig_acc_no,transaction.to,transaction.amount,transaction.time_stamp
            ))






class ATM(Bank):

    def __init__(self, acc_no, pin):

        self.connectDB('bank.db')
        self.auth = False
        #super().__init__()

        Log(Log.BOLD+'\n:::::::::Credentials::::::::::\n'+Log.ENDC)
        if self.login():
            Log(Log.OKGREEN+'\nAccess granted'+Log.ENDC)
        else:
            Log(Log.FAIL+'\nAccess denied'+Log.ENDC)
  
    def login(self, lgn_attempts=1):
        
        _user, _pin = None,  None
        def getInput():
            return [input(Log.BOLD+Log.OKGREEN+'Account number:'+Log.ENDC), input(Log.BOLD+Log.OKGREEN+'pin:'+Log.ENDC)]

        _user, _pin = getInput()

        for key, val in self.accounts.items():
            if key==_user and _pin==val['pin']:
                self.auth=True
               
                return True

        if lgn_attempts==3:
            return False
        
        new_lgn_attempts=lgn_attempts+1

        Log(Log.FAIL+'\nIncorrect creds. please try again ({} attempts left)\n'.format(3-lgn_attempts))

        return self.login(new_lgn_attempts)
    

    def genTransID(self, id=''):
        
        if self.auth:

            id=str(random.randrange(000, 999))+chr(random.randrange(101, 132))+chr(random.randrange(101, 132))+str(random.randrange(000, 999))+chr(random.randrange(101, 132))
            
            if id in self.transactions:
            
                return self.genTransID()

            return id

    def transfer(self, rec_acc_no, orig_acc_no, amount):
        import datetime as date
        if self.auth: 

            t_id=self.genTransID()
            
            transaction = {
                't_id': t_id,
                'rec_acc_no': rec_acc_no,
                'orig_acc_no': orig_acc_no,
                'to': self.accounts[rec_acc_no]['name'], 
                'amount': amount,
                'time_stamp': date.datetime.now()

            }    
            
            if self.accounts[orig_acc_no]['balance'] >= amount:
                self.accounts[orig_acc_no]['balance']-=amount
                self.accounts[rec_acc_no]['balance']+=amount
                
                #self.transactions.update(transaction)
                self._transactions.enqueue(transaction)

                return 'Transaction has been added to queue , t-id: {}, amount: R{}'.format(t_id, amount)

            else:
                return 'Invalid transaction: You do not have enough funds to complete the transfer.'
        else:
            return 'Not authorized to make transactions.'

#b=Bank()
#print(b.accounts)

bank = ATM('639077362', '3465')
'''print(bank.transfer('639077362', '290309379', 200))
print(bank._transactions, '\n')
print(bank.transfer('639077362', '290309379', 50))
print(bank._transactions, '\n')
print(bank.transfer('639077362', '290309379', 10))
print(bank._transactions, '\n')
print(bank.transfer('639077362', '290309379', 21))
print(bank._transactions, '\n\n')
bank.VerifyTransactions()
'''