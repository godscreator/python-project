import pickle

def isLeapYear(year):
    if year % 4 == 0 and year % 100 == 0:
        return True
    else:
        return False
class Log:
    def __init__(self,start,end):
        self.start = start
        self.end   = end
        self.days  = []
        self.names= [] 
        self.logs  = []
        self.initialize(start,end)
    def initialize(self,start,end):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(start,end+1):
            if isLeapYear(i):
                days[1] = 29
            for j in range(1,13):
                if len(str(j))>1:
                    m = str(j)
                else:
                    m = "0"+str(j)
                for k in range(1,days[j-1]+1):
                    if len(str(k))>1:
                        d = str(k)
                    else:
                        d = "0"+str(k)
                    self.days.append(d+m+str(i))
    def append(self,name):
        self.names.append(name)
        self.logs.append([])
        for i in range(len(self.days)):
            self.logs[-1].append(False)
    def check(self,name,date):
        i = self.names.index(name)
        return self.logs[i][self.days.index(date)]
    def set(self,name,date,val):
        i = self.names.index(name)
        self.logs[i][self.days.index(date)] = val
    def Print(self):
        print "Date    ",
        for i in self.names:
            print i,
        print 
        for i in range(len(self.days)):
            print self.days[i],
            for j in range(len(self.names)):
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
