def isLeapYear(year):
    if year % 4 == 0 and year % 100 == 0:
        return True
    else:
        return False
class log:
    def __init__(self, start , end):# start and end are years
        self.cal ={}
        self.initialize(start,end)
    def initialize(self,start,end):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(start,end+1):
            if isLeapYear(year):
                days[1] = 29
            self.cal[i] = {}
            for j in (1,13):
                self.cal[i][j] = []
                for k in range(1,days[j-1]):
                    self.cal[i][j].append(False)
    def get(self,date,month,year):
        try:
            return self.cal[year][month][date-1]
        except :
            return "error"
    def getIn(self,start,end): #start ==> [date,month,year]
        for i in range(start[2],end[2]+1):
            for j in range(start[1],end[1]+1):
                for k in range(start[0],end[0]+1):
                    if self.get(k,j,i) == True:
                        return True
        return False
    def set(self,date,month,year,val):
        try:
             self.cal[year][month][date-1] = val
             return True
        except :
            return "error"
    def setIn(self,start,end): #start ==> [date,month,year]
        for i in range(start[2],end[2]+1):
            for j in range(start[1],end[1]+1):
                for k in range(start[0],end[0]+1):
                     self.set(k,j,i,True) 
        return True
