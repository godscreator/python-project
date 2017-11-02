import pickle
import register
class room:
    def __init__(self):
        self._book = register.log(2000,2200)
        self.type = ""
        self.size = ""
        self.price = 0
        self.cleaning = ""
        self.beds = 0
        self.internet = ""
        self.entertainment = ""
        self.bathroom = ""
        self.air_conditioning = ""
        self.daily_housekeeping = ""
        self.no_of_adults = 0
        self.no_of_children = 0
    def book(self,ind,outd): #  ind = check in date , outd = check out date
         if self._book.getIn(ind,outd) == False:
             self._book.setIn(ind,outd,True)
             return True
         else:
            return False
    def input(self):
        for i in self.__dict__:
            if i[0] != "_":
                self.__dict__ [i] = raw_input(i+" :  ")
    def show(self , spare):
        for i in self.__dict__:
            if i[0] != "_":
               t = str(i)+" : "
               print (spare-len(t))*" " + t + str(self.__dict__[i])
class Hotel:
    def __init__(self):
        self._rooms = []
        self._minprice = 0
        self.location = ""
        self.reservation_policy = ""
        self.type = ""
        self.meal = ""
        self.property_details = ""
        self.area_details = ""
        
    def input(self):
        n = input("Enter no. of rooms : ")
        print "Enter the details of rooms : "
        for i in range(n):
            r = room()
            r.input()
            self._rooms.append(r)
            print "-"*20
        self.setminprice()
        for i in self.__dict__:
            if i[0] != "_":
                self.__dict__ [i] = raw_input(i+" :  ")
    def show(self , spare = 50):
        print "Budget:",self._minprice
        print "Room details:"
        for i in self._rooms:
            i.show(spare)
            print "-"*spare
        for i in self.__dict__:
            if i[0] != "_":
               t = str(i)+" : "
               print (spare-len(t))*" " + t + str(self.__dict__[i])
    def setminprice(self):
        l = [r.price for r in self._rooms]
        self._minprice = min(l)

