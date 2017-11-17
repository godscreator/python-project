import pickle

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

class Log:
    def __init__(self,start,end): 
        self.start = start      # start : year at which log starts.
        self.end   = end        # end   : year at which log ends.
        self.days  = []         # days  : list of days stored in "dd/mm/yyyy".
        self.rooms = []         # rooms : list of roomid.
        self.logs  = []         # logs  : 2D list of userid of ppl booked in roomid and days.
        self.initialize(start,end)
    def initialize(self,start,end):
        # this creates days of log.
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(start,end+1):
            if isLeapYear(i):
                days[1] = 29
            for j in range(1,13):
                for k in range(1,days[j-1]+1):
                    self.days.append(str(k)+"/"+str(j)+"/"+str(i))
    def append(self,roomid):
        # adds a room to the log.
        self.rooms.append(roomid)
        l = []
        for i in range(len(self.days)):
            l.append("")
        self.logs.append(l)
    def pop(self,roomid):
        # delete a room to the log.
        self.rooms.pop(roomid)
        self.logs.pop(roomid)
    def inDays(self,start,end):
        # generator to easily loop over days.
        i = self.days.index(start)
        j = self.days.index(end)
        for k in range(i,j+1):
            yield k
    def getin(self,roomid,indate,outdate):
        # to check if room is booked in btw indate and outdate.
        i = self.rooms.index(roomid)
        for a in self.inDays(indate,outdate):
            if not self.logs[i][a] == "":
                return False
        return True
    def setin(self,roomid,indate,outdate,val):
        # to book in btw indate and outdate.
        i = self.rooms.index(roomid)
        for a in self.inDays(indate,outdate):
            self.logs[i][a] = val
    def Print(self):
        print "Date    ",
        for i in self.rooms:
            print i,
        print 
        for i in range(len(self.days)):
            print self.days[i],
            for j in range(len(self.rooms)):
                print self.logs[j][i],
            print 

def getLog(name):
    f = open(name,"rb")
    log = pickle.load(f)
    f.close()
    return log
def setLog(name,val):
    f = open(name,"wb")
    pickle.dump(val,f)
    f.close()
