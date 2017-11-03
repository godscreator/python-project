import pickle
def isLeapYear(year):
    if year % 4 == 0 and year % 100 == 0:
        return True
    else:
        return False
class log:
    def __init__(self, start =2000, end = 2050):# start and end are years
        self.cal ={}
        self.rooms = []
        self.initialize(start,end)
    def initialize(self,start,end):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(start,end+1):
            if isLeapYear(i):
                days[1] = 29
            self.cal[i] = {}
            for j in range(1,13):
                self.cal[i][j] = {}
                for k in range(1,days[j-1]):
                    self.cal[i][j][k] = []
    def addRoom(self,roomno,hotelname):
        self.rooms.append(hotelname+"_"+roomno)
        for i in self.cal:
            for j in self.cal[i]:
                for k in self.cal[i][j]:
                    self.cal[i][j][k].append(False)
        
    def get(self,date,month,year,roomno = "",hotelname = ""):
        try:
            i = self.rooms.index(hotelname+"_"+roomno)
        except :
            return self.cal[year][month][date-1]
        return self.cal[year][month][date-1][i]
    def getIn(self,start,end): #start ==> [date,month,year]
        r = []
        t =  [False for i in range(len(self.rooms))]
        for i in range(start[2],end[2]+1):
            for j in range(start[1],end[1]+1):
                for k in range(start[0],end[0]+1):
                    v =  self.get(k,j,i)
                    for l in range(len(v)):
                        if v[l] == True:
                            t[l] = True
        for a in range(len(t)):
            if t[a] == False:
                r.append(self.rooms[a])
        return r
    def set(self,date,month,year,roomno,hotelname,val):
        try:
             i = self.rooms.index(hotelname+"_"+roomno)
             self.cal[year][month][date-1][i] = val
             return True
        except :
            print "error in set"
            return "error"
    def setIn(self,start,end,roomno,hotelname,val): #start/end ==> [date,month,year]
        for i in range(start[2],end[2]+1):
            for j in range(start[1],end[1]+1):
                for k in range(start[0],end[0]+1):
                     self.set(k,j,i,roomno,hotelname,val) 
        return True
    
def setRegister(log):
    f = open("register.dat","wb")
    pickle.dump(log,f)
    f.close()
def getRegister():
    f = open("register.dat","rb")
    v  = pickle.load(f)
    f.close()
    return v
