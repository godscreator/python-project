from hotel import *
from styler import *
import pickle

def getHotels():
    f = open("Hotels.dat","rb")
    l = []
    while True:
        try:
            l.append(pickle.load(f))
        except EOFError:
            break
    f.close()
    return l
def setHotels(l,mode = "a"):
    f = open("Hotels.dat",mode+"b")
    for i in l:
        pickle.dump(i,f)
    f.close()
    
def find():
    print "Enter Search details:"
    loc = neoInput("Location : ",notnull = True)
    v = []
    l = getHotels()
    for i in l:
        if i.location == loc:
            v.append(i)
    while True:
        if v:
            print " "*10+"Hotel name"+" "*10+"minimum Price"
            ops ={}
            for i in v:
                if i._rooms!=[]:
                    ops[" "*10+i.name+" "*(20-len(i.name))+"Rs."+str(min([int(j.price) for j in i._rooms]))]=i
            r = menu(options = ops)
            r.show()
            y = raw_input("\nPress Enter to stop seeing search results : ")
            if y:
                continue
            else:
                break
        else:
            print "\n No results found!.."
    return True

def inputHotels():
    while True:
        try:
            a = int(raw_input("Enter no. of hotels : "))
            break
        except ValueError:
            print "Number of hotels should be a number."
    v = []
    for i in range(a):
        h = Hotel()
        h.input()
        v.append(h)
    setHotels(v,"a")
    return True
def modifyHotel():
    hotelname = raw_input("Enter hotel name: ")
    roomno = raw_input("Enter room number: ")
    f = open("Hotels.dat","rb")
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            i.modify()
            break
    else:
        print "no hotel of such name."
    setHotels(l,"w")
    return True
def modifyRoom():
    hotelname = raw_input("Enter hotel name: ")
    roomno = raw_input("Enter room number: ")
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            for j in i._rooms:
                if j._room_no == roomno:
                    j.modify()
                    break
            else:
                print "no such roomno in this hotel."
            break
    else:
        print "no hotel of such name."
    setHotels(l,"w")
    return True
def delHotel():
    hotelname = raw_input("Enter hotel name: ")
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            l.remove(i)
    setHotels(l,"w")
    return True
def delRoom(hotelname,roomno):
    hotelname = raw_input("Enter hotel name: ")
    roomno = raw_input("Enter room number: ")
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            for j in i._room_nos:
                if j==roomno:
                    i.delRoom(j)
                    break
            else:
                print "no such room no."
                break
    else:
        print "no such hotel"
    setHotels(l,"w")
    return True
def Exit():
    return False
def main():
    print"             *******  WELCOME TO BOOKING.PY  *******"
    v = menu(options = {"Find":find,
                        "Input hotels":inputHotels,
                        "Exit":Exit,
                        "Modify hotel":modifyHotel,
                        "Modify room":modifyRoom,
                        "delete room":delRoom,
                        "delete hotel":delHotel,
                        },align = 25)
    return v()
       
while True:
    if main()!=True:
        break

