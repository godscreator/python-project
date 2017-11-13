class Log:
    def __init__(self,start,end):
        self.start = start
        self.end   = end
        self.days  = []
        self.hotels= [] 
        self.logs  = []
    def append(self,hotelname):
        self.hotels.append(hotelname)
        for i in range(len(self.days)):
            self.logs[-1].append(False)
    def check(self,hotelname,date):
        i = self.hotels.index(hotelname)
        return self.logs[i][self.days.index(date)]
    def set(self,hotelname,date,val):
        i = self.hotels.index(hotelname)
        self.logs[i][self.days.index(date)] = val
         
    
