from hotel import *
from styler import *
from user import *
from tables import *
import pickle

User = None

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
def book(name):
    l = getLog("Log.dat")
    print "Check-in-date:"
    d1 = int(raw_input("Date:"))
    m1 = int(raw_input("Month:"))
    y1 = int(raw_input("Year:"))
    cin = d1+"/"+m1+"/"+y1
    print "Check-out-date:"
    d2 = int(raw_input("Date:"))
    m2 = int(raw_input("Month:"))
    y2 = int(raw_input("Year:"))
    cout = d2+"/"+m2+"/"+y2
    g=l.days[l.days.index(cin):l.days.index(cout)]
    for i in g:
        if l.check(name,i):
            print " Room not available"
            break
    else:
        global User
        for i in g:
            l.set(name,i,User.id)
        hotelname,roomno=name.split("_")
        User.book(hotelname,roomno,cin,cout)
        li = getUsers("Users.dat")
        for i in range(len(li)):
            if us.id==li[i].id :
                li[i]=User
                break
        setUsers("Users.dat",li)
        print "Booked !"
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
def Filter():
    print "Enter Filter details:"
    th = template_hotel()
    hot = Hotel()
    l = ["location","type","meal","reservation_policy","area_details"]
    for i in l:
        t = i.title()+" .:  "
        thdict = th.__dict__[i]
        hot.__dict__[i] = neoInput(t,options=thdict["options"],help=thdict["help"],align = 25 ,notnull=False)
    r = room(0,"")
    tr = template_room()
    l = ["no_of_adults","no_of_children","type","size","price","beds","bathroom","air_conditioning","internet","entertainment","housekeeping"]
    for i in l:
        t = i.title()+" .:  "
        trdict = tr.__dict__[i]
        r.__dict__[i] = neoInput(t,options=trdict["options"],help=trdict["help"],align = 25 ,notnull=False)
    hot._rooms=[r]
    v,w = [],[]
    l = getHotels()
    for i in l:
        u = i.match(hot)
        if u:
            v.append(i)
            w.append(u)
    if v:
        while True:
            print " "*10+"Hotel name"+" "*10+"minimum Price"
            ops ={}
            for j in range(len(v)):
                i = v[j]
                if i._rooms!=[]:
                    ops[" "*10+i.name+" "*(20-len(i.name))+"Rs."+str(min([int(j.price) for j in i._rooms]))]=i,w[j]
            r = menu(options = ops)
            r[0].show(r[1])
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
def addRoom():
    hotelname = raw_input("Enter hotel name: ")
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            i.addRoom()
            break
    else:
        print "no hotel of such name."
    setHotels(l,"w")
    
def delHotel():
    hotelname = raw_input("Enter hotel name: ")
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            l.remove(i)
    setHotels(l,"w")
    
def delRoom():
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
    
def Exit():
    return "exit"
def signup():
    l = getUsers("Users.dat")
    us = user()
    us.input()
    for i in l:
        if us.id==i.id :
            print "This id is already in use."
            return True
    l.append(us)
    setUsers("Users.dat",l)
    global User
    User = us
    print "sign up successful!"
    
def signin():
    l = getUsers("Users.dat")
    us = user()
    us.input()
    for i in l:
        if us.id==i.id and us.password==i.password:
            global User
            User = i
            break
    else:
        print "No such user!"
        return True
    print "sign in successful!"
    
def main():
    while True:
        print"             *******  WELCOME TO BOOKING.PY  *******"
        v = menu(options = {"Find":find,
                            "Filter":Filter,
                            "Add room":addRoom,
                            "Sign up":signup,
                            "Sign in":signin,
                            "Input hotels":inputHotels,
                            "Exit":Exit,
                            "Modify hotel":modifyHotel,
                            "Modify room":modifyRoom,
                            "delete room":delRoom,
                            "delete hotel":delHotel,
                            },align = 25,
                 order=["Find","Filter","Sign up","Sign in","Input hotels","Add room",
                        "Modify hotel","Modify room","delete room","delete hotel","Exit"])
        if v() == "exit":
            break

main()

