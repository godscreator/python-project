from styler import *
import pickle
class user:
    def __init__(self):
        self.id=""
        self.name=""
        self.password=""
        self.book = {}#hotelname+roomno:(check-in-date,check-out-date)
    def input(self):
        neoPrint("Enter user details:\n",align=25)
        self.id = neoInput(" id : ",align=25)
        self.name = neoInput(" name : ",align=25)
        self.password = neoInput(" password : ",align=25)
    def book(self,hotelname,roomno,cin,cout):
        self.book[hotelname+"_"+roomno]=(cin,cout)
    def read(self):  
        for i in self.book:
            c = i.split("_")
            print "Hotel name: ",c[0]
            print "Room no.: ",c[1]
            print "Check-in-date",self.book[i][0]
            print "Check-out-date",self.book[i][1]
            print

def getUsers(name):
    l = []
    try:
        f = open(name,"rb")
        while True:
            try:
                l.append(pickle.load(f))
            except EOFError:
                break
        f.close()
    except IOError:
        pass
    return l
def setUsers(name,l):
    f = open(name,"wb")
    for i in l:
        pickle.dump(i,f)
    f.close()