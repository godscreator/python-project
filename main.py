from hotel import *
import pickle
import os
import register
def inputHotels():
    while True:
        try:
            a = int(raw_input("Enter no. of hotels : "))
            break
        except ValueError:
            print "Number of hotels should be a number."
    for i in range(a):
        h = Hotel()
        h.input()
        f = open(h.name+".dat","wb")
        pickle.dump(h,f)
        g = open("hotels.txt","ab")
        g.write(h.name)
        g.close()
        f.close()
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
def search(loc,ind,outd,noa,noc):
    log = register.get()
    t = log.getIn(ind,outd)
    u = [i.partition("_") for i in t]
    v = {} # {hotel name:[rooms]}
    for i in range(len(u)):
        f = open(u[i][0]+".dat","rb")
        hotel = pickle.load(f)
        if hotel.location == loc:
            room = hotel._rooms[hotel._room_nos.index(u[i][2])]
            if room.no_of_adults == str(noa) and room.no_of_children == str(noc):
                if v.has_key(hotel.name):
                    v[hotel.name].append(room)
                else:
                    v[hotel.name] = [room]
        f.close()
    return v
def showResults(v,ind,outd):
    if v == {}:
        print "No results!"
    else:
        for i in v:
            f = open(i+".dat","rb")
            h = pickle.load(f)
            h.show([ind,outd],v[i])
            f.close()



