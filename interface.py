from main import *
import register
print\
"""             *******  WELCOME TO BOOKING.PY  *******"""
mmenu =\
"""************************************************************
                    Main Menu
                    1. Find
                    2. Add hotel
                    3. Add room
                    4. Modify hotel
                    5. Modify room
                    6. Delete hotel
                    7. Delete room
                    0. Exit
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
            hname = raw_input("Enter hotel name:")
            f = open(hname+".dat","rb")
            h = pickle.load(f)
            f.close()
            h.addRoom()
            f = open(hname+".dat","wb")
            pickle.dump(h,f)
            f.close()
        elif c == "4":
            hname = raw_input("Enter hotel name:")
            modifyHotel(hname)
        elif c=="5":
            hname = raw_input("Enter hotel name:")
            roomno = raw_input("Enter room no:")
            modifyRoom(hname,roomno)
        elif c == "6":
            hname = raw_input("Enter hotel name:")
            delHotel(hname)
        elif c=="7":
            hname = raw_input("Enter hotel name:")
            roomno = raw_input("Enter room no:")
            delRoom(hname,roomno)
        elif c == "0":
            break
        else:
            print "Wrong Choice"
       
            
def find():
    print "Enter Search details:"
    while True:
        loc = raw_input("Location : ")
        if not(loc):
            print "Location not entered."
            continue
        break
    while True:
        try :
            ind = [int(i) for i in raw_input("Check in date : ").split("-")]
            outd = [int(i) for i in raw_input("Check out date : ").split("-")]
            break
        except ValueError:
            print "Sorry! Date should be in format dd-mm-yyyy"
    while True:
        try:
            noa = int(raw_input("No. of  adults : "))
            noc = int(raw_input("No. of  children : "))
            break
        except ValueError:
            print "Sorry! number of adults and children should be a number."
    v = search(loc,ind,outd,str(noa),str(noc))
    if not(v):
        print "\n No results found!.."
        return 0
    while True:
        print " "*10+"Hotel name"+" "*10+"minimum Price"
        for i in v:
            print " "*10+i+" "*(20-len(i))+"Rs."+str(min([j.price for j in v[i]]))
        y = raw_input("\nSee hotels : ")
        if y:
            x = raw_input("\nEnter name of hotel : ")
            try:
                showResults({x:v[x]},ind,outd)
            except KeyError:
                print "Sorry ! no hotel of given name."
        else:
            break
    
main()
