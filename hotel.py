from styler import *
from template import *
class room:
    def __init__(self,roomno,hotelname):
        self._hotel_name = hotelname
        self._room_no = roomno
        self.no_of_adults = 0
        self.no_of_children = 0
        self.type = ""
        self.size = ""
        self.price = 0
        self.beds = 0
        self.bathroom = ""
        self.air_conditioning = ""
        self.internet = ""
        self.entertainment = ""
        self.housekeeping = ""
    
    def input(self):
        tr = template_room()
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
            t = i.title()+" :  "
            trdict = tr.__dict__[i]
            self.__dict__ [i] = neoInput(t,options=trdict["options"],help=trdict["help"],align = 25 ,notnull=True)
            print
        
        
    def modify(self):
        tr = template_room()
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
            t = i.title()+" .:  "
            trdict = tr.__dict__[i]
            v = neoInput(t,options=trdict["options"],help=trdict["help"],align = 25 ,notnull=False)
            if v:
                self.__dict__ [i] = v
            print
        
    def show(self):
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
           t = i.title()+" : "
           neoPrint (t,align = 25)
           print self.__dict__[i]
        
        

class Hotel:
    def __init__(self):
        self._rooms = []
        self._room_nos = []
        self.name =""
        self.location = ""
        self.type = ""
        self.meal = ""
        self.reservation_policy = ""
        self.property_details = ""
        self.area_details = ""
        
    def input(self):
        self.name = neoInput("Name .:  ",align=25,notnull = True)
        print 
        th = template_hotel()
        l = ["location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
            t = i.title()+" :  "
            thdict = th.__dict__[i]
            self.__dict__ [i] = neoInput(t,options=thdict["options"],help=thdict["help"],align = 25 ,notnull=True)
            print
        def noofrooms():
            try:
                n = int(neoInput("Enter no. of rooms : ",align = 25,notnull = True))
                return n
            except ValueError:
                print "room no. should be a number"
                return False
        n = infinite(noofrooms,br = False)
        for i in range(n):
            neoPrint("Enter the details of rooms : \n\n",align = 25)
            self.addRoom()
            
    def addRoom(self):
        rno = neoInput("Enter the room number: ",align = 25,notnull = True)
        print
        r = room(rno,self.name)
        r.input()
        self._room_nos.append(rno)
        self._rooms.append(r)
        print "-"*70
        
    def delRoom(self,rno):
        i = self._room_nos.index(rno)
        self._room_nos.pop(i)
        self._rooms.pop(i)
        
    def delHotel(self):
        for i in self._room_nos:
            self.delRoom(i)
            
    def modify(self):
        th = template_hotel()
        l = ["location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
            t = i.title()+" .:  "
            thdict = th.__dict__[i]
            v = neoInput(t,options=thdict["options"],help=thdict["help"],align = 25 ,notnull=False)
            if v:
                self.__dict__ [i] = v
            print
        
    def show(self,rooms = "ALL"):
        print "*"*60
        if rooms == "ALL":
            rooms = self._rooms
        l = ["name","location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
           t = i.title()+" : "
           neoPrint (t,align = 25)
           print self.__dict__[i]
        print "\nRoom details:"
        for i in rooms:
            i.show()
            print "-"*60

