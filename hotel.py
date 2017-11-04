import pickle
import register
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
       
    def book(self,ind,outd): #  ind = check in date , outd = check out date
         log = register.get()
         log.setIn(ind,outd,self._room_no,self._hotel_name,True)
         register.set(log)

    def input(self,space = 30):
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
            t = i.title()+" :  "
            self.__dict__ [i] = raw_input((space-len(t))*" "+t)
        log = register.get()
        log.addRoom(self._room_no,self._hotel_name)
        register.set(log)
        
    def modify(self,space =30 ):
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
            t = i.title()+" .:  "
            v = raw_input((space - len(t))*" "+t)
            if v:
                self.__dict__ [i] = v
        
    def show(self ,Book =[]  ,space = 0):
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
           t = i.title()+" : "
           print (space-len(t))*" " + t + str(self.__dict__[i])
        if Book:
            g = raw_input("\n Book now:")
            if g !="no" and g!="n" and g:
                self.book(Book[0],Book[1])
                print "Booking Complete!.."

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
        
    def input(self,space = 30):
        while True:
            hn = raw_input(" "*21+"Name .:  ")
            if hn:
                g = open("hotels.txt","rb")
                nlist = g.readlines()
                g.close()
                flag = True
                for co in nlist:
                    if hn == co:
                       flag = False
                if flag:
                    break
            else :
                print "no name entered"
        l = ["location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
            t = i.title()+" .:  "
            self.__dict__ [i] = raw_input((space-len(t))*" "+t)
        while True:
            try:
                n = int(raw_input("Enter no. of rooms : "))
                break
            except ValueError:
                print "room no. should be a number"    
        for i in range(1,n+1):
            print "Enter the details of rooms : "
            self.addRoom()
            
    def addRoom(self):
        rno = raw_input("Enter the room number:")
        r = room(rno,self.name)
        r.input()
        self._room_nos.append(rno)
        self._rooms.append(r)
        print "-"*70
    def delRoom(self,rno):
        i = self._room_nos.index(rno)
        self._room_nos.pop(i)
        self._rooms.pop(i)
        log = register.get()
        log.delRoom(rno,self.name)
        register.set(log)
    def delHotel(self):
        for i in self._room_nos:
            self.delRoom(i)
    def modify(self,space=30):
        l = ["location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
            t = i.title()+" .:  "
            v = raw_input((space-len(t))*" "+t)
            if v:
                self.__dict__ [i] = v
        
    def show(self ,Book =[],rooms = "ALL", space = 30):
        print "*"*space
        if rooms == "ALL":
            rooms = self._rooms
        l = ["name","location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
           t = str(i)+" .: "
           print (space-len(t))*" " + t.title() + str(self.__dict__[i])
        print "\nRoom details:"
        for i in rooms:
            i.show(Book,space)
            print "-"*space*2
