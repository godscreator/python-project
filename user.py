from styler import *
import pickle
gspace = 50
class user:
    def __init__(self):
        self.id=""
        self.password=""
        self.book = []#[hotelname,roomno,check-in-date,check-out-date]
    def input(self):
        neoPrint("Enter user details:\n",align=gspace)
        self.id = neoInput(" id : ",align=gspace)
        self.password = neoInput(" password : ",align=gspace)
    def Book(self,hotelname,roomno,cin,cout):
        self.book.append([hotelname,roomno,cin,cout])
    def read(self):
        if not self.book:
            neoPrint("Error: No data to display.",align=gspace)
        for i in self.book:
            neoPrint("Hotel name : ",align=gspace)
            print i[0]
            neoPrint("Room no. : ",align=gspace)
            print i[1]
            neoPrint("Check-in-date",align=gspace)
            print i[2]
            neoPrint("Check-out-date",align=gspace)
            print i[3]
            print

def getUsers(name):
    try:
        f = open(name,"rb")
        l = pickle.load(f)
    except (IOError,EOFError):#in case no users registered.
        setUsers(name,[])
        l = getUsers(name)
    f.close()
    return l
def setUsers(name,l):
    f = open(name,"wb")
    pickle.dump(l,f)
    f.close()
