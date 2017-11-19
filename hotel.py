from styler import *
from template import *
from tables import *
from user import *
gspace=50
class room:
    # class variables.
    order = ["no_of_adults","no_of_children","type","size","price","beds","bathroom",              # represents order in
             "air_conditioning","internet","entertainment","housekeeping"]                         # which data is presented.
    temp  = template_room() # represents template of room.
    def __init__(self,roomid,hotelid):
        self._hotelid           = hotelid
        self._roomid            = roomid
        self.no_of_adults       = 0
        self.no_of_children     = 0
        self.type               = ""
        self.size               = ""
        self.price              = 0
        self.beds               = 0
        self.bathroom           = ""
        self.air_conditioning   = ""
        self.internet           = ""
        self.entertainment      = ""
        self.housekeeping       = ""
    
    def input(self):
        for i in room.order:
            self.__dict__[i] = neoInput(i.replace("_"," ").title()+" :  ",align = gspace ,notnull=True,**room.temp.__dict__[i])
        
    def modify(self):
        l = menu(room.order,room.order,align = gspace,select=True)
        for i in l:
            v = neoInput((i.replace("_"," ")).title()+" :  ",align = gspace ,notnull=False,**room.temp.__dict__[i])
            if v:
                self.__dict__ [i] = v

    def match(self,other):
        for i in room.order:
            v = other.__dict__[i]
            if v :
                if self.__dict__[i] != v:
                    try:
                        if not v  in self.__dict__[i]:
                            return False
                    except TypeError:
                        return False
        else:
            return True

    def book(self,ind,outd,userid):
        l = getLog("Log.dat")
        l.setin(str(self._hotelid)+"_"+str(self._roomid),ind,outd,userid)
        setLog("Log.dat",l)

    def show(self):
        for i in room.order+["_roomid"]:
           neoPrint ((i.replace("_"," ")).title()+" : ",align = gspace)
           print self.__dict__[i]
        
        

class Hotel:
    # class variables.
    order = ["name","location","type","meal","reservation_policy","property_details","area_details"]
    temp  = template_hotel()
    def __init__(self):
        self._hotelid           = 0
        self._rooms             = []
        self._roomids           = []
        self.name               = ""
        self.location           = ""
        self.type               = ""
        self.meal               = ""
        self.reservation_policy = ""
        self.property_details   = ""
        self.area_details       = ""
        
    def input(self):
        for i in Hotel.order:
            self.__dict__ [i] = neoInput((i.replace("_"," ")).title()+" : ",align = gspace ,notnull=True,**Hotel.temp.__dict__[i])
        while True:
            try:
                n = int(neoInput("Enter no. of rooms : ",align = gspace,notnull = True))
                break
            except ValueError:
                neoPrint("Error: room no. should be a number",align = gspace)
        for i in range(n):
            neoPrint("Enter the details of rooms : \n\n",align = gspace)
            self.addRoom()
            
    def addRoom(self):
        if len(self._roomids)>0:
            k = self._roomids[-1]+1
        else:
            k = 0
        r = room(k,self._hotelid)
        r.input()
        self._rooms.append(r)
        self._roomids.append(k)
        l = getLog("Log.dat")
        try:
            i = l.rooms.index(str(self._hotelid)+"_"+str(k))
            l.rooms.pop(i)
            l.logs.pop(i)
        except ValueError:
            pass
        l.append(str(self._hotelid)+"_"+str(k))
        setLog("Log.dat",l)
        
    def delRoom(self,roomid):
        self._rooms.pop(self._roomids.index(roomid))
        self._roomids.remove(roomid)
        l = getLog("Log.dat")
        l.pop(str(self._hotelid)+"_"+str(roomid))
        setLog("Log.dat",l)

    def delHotel(self):
        for i in self._roomids:
            self.delRoom(i)
              
    def modify(self):
        l = menu(Hotel.order,Hotel.order,align = gspace,select=True)
        for i in l:
            v = neoInput((i.replace("_"," ")).title()+" : ",align = gspace ,notnull=False,**Hotel.temp.__dict__[i])
            if v:
                self.__dict__ [i] = v

    def match(self,other):
        for i in Hotel.order:
            v = other.__dict__[i]
            if v:
                if self.__dict__ [i] != v:
                    try:
                        if v not in self.__dict__ [i]:
                            return []
                    except TypeError:
                        return []
        else:
            k = []
            for i in range(len(self._rooms)):
                if self._rooms[i].match(other._rooms[0]):
                    k.append(self._roomids[i])
            return k
        
    def show(self,roomids = "ALL",Book=[]):#Book = [indate,outdate,userid]
        print " "*20+"*"*60
        if roomids == "ALL":
            rooms = self._rooms
        else:
            rooms = []
            for i in roomids:
                rooms.append(self._rooms[self._roomids.index(i)])
        for i in Hotel.order:
           neoPrint ((i.replace("_"," ")).title()+" : ",align = 50)
           print self.__dict__[i]
        print
        neoPrint("Room details :\n",align=30)
        for i in rooms:
            print " "*20+"-"*60
            i.show()
            if Book:
                g = neoInput("\n Book now (y/n):",align=gspace)
                if g=="y":
                    i.book(*Book)
                    bn=getUsers("Users.dat")
                    for j in bn:
                        if j.id == Book[2]:
                            j.Book(self.name,str(i._roomid),Book[0],Book[1])
                    setUsers("Users.dat",bn)
                    neoPrint("Booking complete!..",align=gspace)
            print " "*20+"-"*60
        print " "*20+"*"*60

def getHotels():
    f = open("Hotels.dat","rb")
    try:
        l=pickle.load(f)
    except EOFError:
        l=[]
    f.close()
    return l
def setHotels(l):
    f = open("Hotels.dat","wb")
    pickle.dump(l,f)
    f.close()
