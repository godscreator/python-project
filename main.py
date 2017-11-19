from hotel import *
from styler import *
from user import *
from tables import *
import pickle
gspace  = 50
User    = None # denotes current user.
Sea     = None # denotes current search results.
gcin    = None # denotes current check in date user is looking for.
gcout   = None # denotes current check out date user is looking for.
def showResults(v,ind = gcin,outd = gcout):
    while True:
        if v:
            ops =[]
            vls =[]
            for i in v:
                l = []
                for j in v[i]:
                    l.append(i._rooms[i._roomids.index(j)].price)
                ops.append(" "*15+i.name+" "*(30-len(i.name))+"Rs."+str(min(l)))
                vls.append(i)
            r = menu(ops,vls,head=" "*65+"Hotel name"+" "*20+"minimum Price",align=gspace)
            if User:
                k = [ind,outd,User.id]
            else:
                k = []
            r.show(roomids=v[r],Book=k)
            updateUser()
            y = neoInput("\nPress Enter to stop seeing search results : ",align=gspace)
            if y:
                continue
            else:
                break
        else:
            neoPrint("\n No results found!..",align=gspace)
            break
def find():
    neoPrint("Enter Search details :\n",align=gspace)
    loc  = neoInput("Location : ",notnull=True,align=gspace)
    cin  = neoInput("Check in date : " ,help="format=\'dd/mm/yyyy\'",notnull=True,align=gspace)
    cout = neoInput("Check out date : ",help="format=\'dd/mm/yyyy\'",notnull=True,align=gspace)
    LOG = getLog("Log.dat")
    if cin not in LOG.days:
        neoPrint("Error: check in date is wrong\n",align=gspace)
        print
        return 0
    if cout not in LOG.days:
        neoPrint("Error: check out date is wrong\n",align=gspace)
        print
        return 0
    v = {}
    l = getHotels()
    for i in l:
        if i.location == loc:
            for j in i._rooms:
                if LOG.getin(str(i._hotelid)+"_"+str(j._roomid),cin,cout):
                   if v.has_key(i):
                       v[i].append(j._roomid)
                   else:
                       v[i]=[j._roomid]
    global Sea,gcin,gout
    Sea,gcin,gout = v,cin,cout
    showResults(v,cin,cout)

    
def Filter(sea="prev"):
    if sea =="prev":
        if not Sea:
            neoPrint("Error: no search previously done.\n",align=gspace)
            return 0
    neoPrint("Enter Filter details:\n",align=gspace)
    hot = Hotel()
    hot.modify()
    r = room("",0)
    r.modify()
    hot._rooms=[r]
    v = Sea
    w = {}
    l = getHotels()
    for i in v:
        u = i.match(hot)
        if u:
            w[i]=u
    showResults(w,gcin,gcout)

def inputHotels():
    v= getHotels()
    while True:
        try:
            a = int(neoInput("Enter no. of hotels : \n",align=gspace))
            break
        except ValueError:
            neoPrint("Error: Number of hotels should be a number.\n",align=gspace)
    for i in range(a):
        h = Hotel()
        h.input()
        v.append(h)
    setHotels(v)
def modifyHotel():
    hotelname = neoInput("Enter hotel name: \n",align=gspace)
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            i.modify()
            break
    else:
        neoPrint("Error: no hotel of such name.\n",align=gspace)
    setHotels(l)
   
def modifyRoom():
    hotelname = neoInput("Enter hotel name: \n",align=gspace)
    roomno = neoInput("Enter room number: \n",align=gspace)
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            for j in i._rooms:
                if j._roomid == int(roomno):
                    j.modify()
                    break
            else:
                neoPrint("Error: no such roomno in this hotel.\n",align=gspace)
            break
    else:
        neoPrint("Error : no hotel of such name.\n",align=gspace)
    setHotels(l)
    
def addRoom():
    hotelname = neoInput("Enter hotel name: ",align=gspace)
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            i.addRoom()
            break
    else:
        neoPrint("Error:no hotel of such name.\n",align=gspace)
    setHotels(l)
    
def delHotel():
    hotelname = neoInput("Enter hotel name: \n",align=gspace)
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            i.delHotel()
            l.remove(i)
    setHotels(l)
    
def delRoom():
    hotelname = neoInput("Enter hotel name: \n",align=gspace)
    roomno = neoInput("Enter room number: \n",align=gspace)
    l = getHotels()
    for i in l:
        if i.name == hotelname:
            try:
                i.delRoom(int(roomno))
            except ValueError:
                neoPrint("Error:no such room no.\n",align=gspace)
            break
    else:
        neoPrint("no such hotel\n",align=gspace)
    setHotels(l)
    
def Exit():
    return "exit"
def signup():
    l = getUsers("Users.dat")
    us = user()
    us.input()
    for i in l:
        if us.id==i.id :
            neoPrint("This id is already in use.\n",align=gspace)
            return True
    l.append(us)
    setUsers("Users.dat",l)
    global User
    User = us
    neoPrint("sign up successful!\n",align=gspace)
    
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
        neoPrint("No such user!\n",align=gspace)
        return True
    neoPrint("sign in successful!\n",align=gspace)
def updateUser():
    global User
    bn = getUsers("Users.dat")
    for i in bn:
        if User:
            if i.id==User.id:
                User.book=i.book
                break
def readUser():
    if User:
        User.read()
    else:
        neoPrint("Error: no one signed in.\n",align=gspace)
def main():
    while True:
        print"""                                          
=====================================================================================================================================
                                                 HOTEL Query      
====================================================================================================================================="""
        v = menu(vals =[find,Filter,signup,signin,readUser,inputHotels,addRoom,modifyHotel,modifyRoom,delRoom,delHotel,Exit],
                 options=["Find","Filter","Sign up","Sign in","My account","Input hotels","Add room",
                        "Modify hotel","Modify room","delete room","delete hotel","Exit"],head="Main menu",align = gspace)
        if v() == "exit":
            break

main()

