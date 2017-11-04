from main import *
print\
"""                         *******  WELCOME TO BOOKING.PY  *******"""
mmenu =\
"""
                                                        Main Menu
                                                        1. Find
                                                        2. Add hotel
                                                        3. Add room
                                                        4. Modify hotel
                                                        5. Modify room
                                                        6. Exit
"""
def main():
    while True:
        print mmenu
        c = raw_input("Enter your choice:")
        if c=="1":
            find()
        elif c == "2":
            inputHotels()
        elif c== "3":
            pass
        elif c == "4":
            hname = raw_input("Enter hotel name:")
            modifyHotel(hname)
        elif c=="5":
            hname = raw_input("Enter hotel name:")
            roomno = raw_input("Enter room name:")
            modifyRoom(hname,roomno)
        elif c == "6":
            break
        else:
            print "Wrong Choice"
            
def find():
    print "Enter Search details:"
    loc = raw_input(" Location : ")
    ind = [int(i) for i in raw_input("Check in date : ").split("-")]
    outd = [int(i) for i in raw_input("Check out date : ").split("-")]
    noa = raw_input("No. of  adults : ")
    noc = raw_input("No. of  children : ")
    v = search(loc,ind,outd,noa,noc)
    print "                 Hotel name                  minimum Price"
    for i in v:
        print     "\t",i,"                                    Rs.",min([j.price for j in v[i]])
    x = raw_input("Enter name of hotel : ")
    if x:
        showResults({x:v[x]},ind,outd)
main()
