from styler import *
from template import *
from tables import *

class room:
    # class variables.
    order = ["no_of_adults","no_of_children","type","size","price","beds",              # represents order in
             "bathroom","air_conditioning","internet","entertainment","housekeeping"]   # which data is presented.
    temp  = template_room() # represents template of room.
    def __init__(self,roomid,hotelid):
        self._hotelid = hotelid
        self._roomid = roomid
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
        for i in room.order:
            self.__dict__ [i] = neoInput(i+" :  ",
            options=room.temp.__dict__[i]["options"],help=room.temp.__dict__[i]["help"],align = 25 ,notnull=True)
        
    def modify(self):
        for i in room.order:
            v = neoInput(i+" :  ",
            options=room.temp.__dict__[i]["options"],help=room.temp.__dict__[i]["help"],align = 25 ,notnull=False)
            if v:
                self.__dict__ [i] = v

    def match(self,other):
        for i in room.order:
            v = other.__dict__[i]
            if v != "":
                if self.__dict__ [i] != v:
                    if len(self.__dict__ [i])>1:
                        if v not in self.__dict__ [i]:
                            return False
                    else:
                        return False
        else:
            return True
    def book(self,ind,outd,userid):
        l = getLog("Log.dat")
        l.book(hid+"_"+rid,ind,outd,userid)
        setLog("Log.dat",l)
    def show(self):
        for i in room.order:
           neoPrint (i+" : ",align = 25)
           print self.__dict__[i]
        
        

class Hotel:
    # class variables.
    order = ["name","location","type","meal","reservation_policy","property_details","area_details"]
    temp  = template_hotel()
    def __init__(self):
        self._hotelid = 0
        self._rooms = []
        self.name =""
        self.location = ""
        self.type = ""
        self.meal = ""
        self.reservation_policy = ""
        self.property_details = ""
        self.area_details = ""
        
    def input(self):
        for i in Hotel.order:
            self.__dict__ [i] = neoInput(i+" :  ",
            options=Hotel.temp.__dict__[i]["options"],help=Hotel.temp.__dict__[i]["help"],align = 25 ,notnull=True)
        while True:
            try:
                n = int(neoInput("Enter no. of rooms : ",align = 25,notnull = True))
                break
            except ValueError:
                print "room no. should be a number"
        for i in range(n):
            neoPrint("Enter the details of rooms : \n\n",align = 25)
            self.addRoom()
            
    def addRoom(self):
        r = room(len(self._rooms),self._hotelid)
        r.input()
        self._rooms.append(r)
        l = getLog("Log.dat")
        l.append(str(self._hotelid)+"_"+str(len(self._rooms)))
        setLog("Log.dat",l)
        print "-"*70
        
    def delRoom(self,roomid):
        self._rooms.pop(roomid)
        l = getLog("Log.dat")
        l.pop(str(self._hotelid)+"_"+str(len(self._rooms)))
        setLog("Log.dat",l)
            
    def modify(self):
        for i in Hotel.order:
            v = neoInput(i+" :  ",
            options=Hotel.temp.__dict__[i]["options"],help=Hotel.temp.__dict__[i]["help"],align = 25 ,notnull=False)
            if v:
                self.__dict__ [i] = v

    def match(self,other):
        for i in Hotel.order:
            v = other.__dict__[i]
            if v:
                if self.__dict__ [i] != v:
                    if len(self.__dict__ [i])>1:
                        if v not in self.__dict__ [i]:
                            return []
                    else:
                        return []
        else:
            k = []
            for i in range(len(self._rooms)):
                if self._rooms[i].match(other._rooms[0]):
                    k.append(i)
            return k
        
    def show(self,roomids = "ALL",Book=[]):#Book = [indate,outdate,userid]
        print "*"*60
        if roomids == "ALL":
            rooms = self._rooms
        else:
            rooms = []
            for i in roomids:
                rooms.append(self._rooms[i])
        for i in Hotel.order:
           neoPrint (i+" : ",align = 25)
           print self.__dict__[i]
        print "\nRoom details:"
        for i in rooms:
            print "-"*60
            i.show()
            if Book:
                g = raw_input("\n Book now (y/n):")
                if g=="y":
                    i.book(*Book)
                    print "Booking complete!.."
            print "-"*60
        print "*"*60

def getHotels():
    f = open("Hotels.dat","rb")
    l=pickle.load(f)
    f.close()
    return l
def setHotels(l):
    f = open("Hotels.dat","wb")
    pickle.dump(l,f)
    f.close()
