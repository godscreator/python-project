import pickle
import register
class room:
    def __init__(self):
        self._book_ = register.log(2000,2050)
        self._hotel_ = None
        self._roomno = ""
        self._no_of_adults = 0
        self._no_of_children = 0
        self.type = ""
        self.size = ""
        self.price = 0
        self.beds = 0
        self.bathroom = ""
        self.air_conditioning = ""
        self.internet = ""
        self.entertainment = ""
        self.housekeeping = ""
       
    def book(self,ind,outd): #  ind = check in date , outd = check out date
         if self._book_.getIn(ind,outd) == False:
             self._book_.setIn(ind,outd,True)
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
        self.name =""
        self.location = ""
        self.type = ""
        self.meal = ""
        self.reservation_policy = ""
        self.property_details = ""
        self.area_details = ""
        
    def input(self):
        n = input("Enter no. of rooms : ")
        print "Enter the details of rooms : "
        for i in range(n):
            r = room()
            r._hotel = self
            r.input()
            self._rooms.append(r)
            print "-"*20
        for i in self.__dict__:
            if i[0] != "_":
                self.__dict__ [i] = raw_input(i+" :  ")
    def show(self ,rooms, spare = 20):
        print "Room details:"
        for i in rooms:
            i.show(spare)
            print "-"*spare*2
        for i in self.__dict__:
            if i[0] != "_":
               t = str(i)+" : "
               print (spare-len(t))*" " + t + str(self.__dict__[i])
