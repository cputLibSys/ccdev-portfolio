import sys
import path 
import os 
import datetime
import pytz 

sys.path.append(os.path.abspath("../"))
from Log import Log

class Guard():

    def __init__(self):
        self._file=None
    
        if os.path.exists("./syslog.info"):
            self._file=open("syslog.info", "w+")

        else:

            self._file=open("syslog.info", "w")


    def logAuth(self, user):
        _date=datetime.datetime.now(pytz.timezone("Africa/Johannesburg"))
        _time=_date.strftime("%X")
        _date=_date.strftime("%x")
        self._file.write(Log.OKGREEN+"User [{}] logedin at {} on {}: SessId - }".format(user.name, _time, _date, user.session_id)+Log.ENDC)
        self._file.close()

auth=Guard()
auth.logAuth("root")
