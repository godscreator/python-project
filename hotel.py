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
         log = register.getRegister()
         log.setIn(ind,outd,self._room_no,self._hotel_name,True)
         register.setRegister(log)

    def input(self):
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
            if i[0] != "_":
                self.__dict__ [i] = raw_input(i.title()+" :  ")
        log = register.getRegister()
        log.addRoom(self._room_no,self._hotel_name)
        register.setRegister(log)
    def show(self ,ind,outd ,spare):
        l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
        for i in l:
            if i[0] != "_":
               t = str(i.title())+" : "
               print (spare-len(t))*" " + t + str(self.__dict__[i])
        g = raw_input("\n Book now:")
        if g !="no" and g!="n" and g:
            self.book(ind,outd)
            print "Done!.."
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
        l = ["name","location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
            if i[0] != "_":
                self.__dict__ [i] = raw_input(i.title()+" .:  ")
        n = input("Enter no. of rooms : ")
        print "Enter the details of rooms : "
        for i in range(1,n+1):
            rno = raw_input("Enter the room number:")
            r = room(rno,self.name)
            r.input()
            self._room_nos.append(rno)
            self._rooms.append(r)
            print "-"*20
    def show(self ,ind,outd,rooms, spare = 25):
        l = ["name","location","type","meal","reservation_policy","property_details","area_details"]
        for i in l:
            if i[0] != "_":
               t = str(i)+" .: "
               print (spare-len(t))*" " + t.title() + str(self.__dict__[i])
        print "\nRoom details:"
        for i in rooms:
            i.show(ind,outd,spare)
            print "-"*spare*2
