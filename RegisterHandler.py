import pickle
def isLeapYear(year):
    if year % 4 == 0 and year % 100 == 0:
        return True
    else:
        return False
    
def getDateIndex(date,month,log):
    try:
        return log[0].index(str(date)+"/"+str(month))
    except IndexError:
        return False
    
def isValidDate(date,log): # date ==> [date,month,year]
    if str(log[0][0]) == str(date[2]):
        if getDateIndex(date[0],date[1],log):
            return True
        else:
            return False
    else:
        return False

def printlog(log):
    for i in log:
        for j in i:
            print j,
        print
        
def initialize(year):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        days[1] = 29
    log = [[]]
    log[0][0] = year
    for i in range(1,13):
        for j in range(1,days[i-1]):
            log[0].append(str(j)+"/"+str(i))
    f = open(str(year)+".register","wb")
    pickle.dump(log,f)
    f.close()
            
def addRoom(rid,hid,log):
    log.append(hid+"_"+rid)
    for i in self.cal:
        for j in self.cal[i]:
            for k in self.cal[i][j]:
                self.cal[i][j][k].append(False)
def delRoom(self,roomno,hotelname):
    a = self.rooms.index(hotelname+"_"+roomno)
    for i in self.cal:
        for j in self.cal[i]:
            for k in self.cal[i][j]:
                self.cal[i][j][k].pop(a)
    self.rooms.pop(a)
def getIn(self,start,end): #start/end ==> [date,month,year]
    if self.isValidDate(start) and self.isValidDate(end):
        t =  [False for i in range(len(self.rooms))] # initial list , assuming no room is booked.
        for i in range(start[2],end[2]+1): # year
            for j in range(start[1],end[1]+1): # month
                for k in range(start[0],end[0]+1): # days
                    v =  self.cal[i][j][k-1]
                    for l in range(len(v)):
                        if v[l] == True:    # if booked already then correcting initial list
                            t[l] = True
        r = [] # list to contain non-booked rooms id.
        for a in range(len(t)):
            if t[a] == False:
                r.append(self.rooms[a])
        return r
    else:
        print "Invalid date entered.. (note:date should be within year 2000 and 2050)"
        return []

def setIn( log , cin , cout , rid , hid ) :  #start/end ==> [date,month,year]
    for i in range(cin[2],cout[2]+1):
        for j in range(cin[1],cout[1]+1):
            for k in range(cin[0],cout[0]+1):
                 l = self.rooms.index(hotelname+"_"+roomno)
                 self.cal[i][j][k-1][l] = val


def savelog(func):
    def inner(*args,**kwargs):
        f = open("year.register","rb")
        kwargs["log"]  = pickle.load(f)
        f.close()
        v = func(*args,**kwargs)
        f = open("year.register","wb")
        pickle.dump(kwargs["log"],f)
        f.close()
        return v
    return inner
    
