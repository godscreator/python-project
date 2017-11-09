from hotel import *
from styler import *
import pickle
import os

           
def find():
    print "Enter Search details:"
    loc = neoInput("Location : ",notnull = True)
    v = []
    f = open("Hotels.dat","rb")
    while True:
        try:
            obj = pickle.load(f)
            if obj.location == loc:
                v.append(obj)
        except EOFError:
            break
    f.close()
    def func():
        if v:
            print " "*10+"Hotel name"+" "*10+"minimum Price"
            ops ={}
            for i in v:
                ops[" "*10+i.name+" "*(20-len(i.name))+"Rs."+str(min([j.price for j in v[v.index(i)]._rooms]))]=i
            r = menu(options = ops)
            r.show()
            y = raw_input("\nSee hotels : ")
            if y:
                func()
            else:
                return "break"
        else:
            print "\n No results found!.."
    k = infinite(func,br = "break")
    return "loop"

def inputHotels():
    while True:
        try:
            a = int(raw_input("Enter no. of hotels : "))
            break
        except ValueError:
            print "Number of hotels should be a number."
    f = open("Hotels.dat","ab")
    for i in range(a):
        h = Hotel()
        h.input()
        pickle.dump(h,f)  
    f.close()
    return "loop"
def modifyHotel(hotelname):
    f = open(hotelname+".dat","rb")
    l = pickle.load(f)
    f.close()
    l.modify()
    f = open(hotelname+".dat","wb")
    pickle.dump(l,f)
    f.close()
def modifyRoom(hotelname,roomno):
    f = open(hotelname+".dat","rb")
    l = pickle.load(f)
    f.close()
    i = l._room_nos.index(roomno)
    r = l._rooms[i]
    r.modify()
    f = open(hotelname+".dat","wb")
    pickle.dump(l,f)
    f.close()
def delHotel(hotelname):
    f = open(hotelname+".dat","rb")
    l = pickle.load(f)
    f.close()
    l.delHotel()
    os.remove(hotelname+".dat")
def delRoom(hotelname,roomno):
    f = open(hotelname+".dat","rb")
    l = pickle.load(f)
    f.close()
    l.delRoom(roomno)
    f = open(hotelname+".dat","wb")
    pickle.dump(l,f)
    f.close()
def Exit():
    return "exit"
def main():
    print"             *******  WELCOME TO BOOKING.PY  *******"
    v = menu(options = {"Find":find,"Input hotels":inputHotels,"Exit":Exit},align = 25)
    return v()
       
infinite(main, br = "loop")

