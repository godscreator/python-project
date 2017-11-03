from hotel import *
import pickle
def search(hotels,loc,ind,outd,noa,noc):
    t = []
    for i in hotels :
        if i.location == loc :
            u = []
            for j in i._rooms:
                if j._book.getIn(ind,outd) == False and noa == j.no_of_adults and noc == j.no_of_children:
                    u.append(j)
            if len(u) > 0:
                t.append(u)
    return t
##f = open("hotel.dat","ab")
##a = input("Enter no. of hotels :")
##for i in range(a):
##    h = Hotel()
##    h.input()
##    pickle.dump(h,f)
##f.close()
f = open("hotel.dat","rb")
hotels = []
while True:
    try:
        hotels.append(pickle.load(f))
    except EOFError:
        break        
f.close()
print "Enter Search details:"
loc = raw_input("Enter Location:")
ind = eval(raw_input("check in date"))
outd = eval(raw_input("check out date"))
noa = raw_input("Enter no of adults:")
noc  = raw_input("Enter no of children:")
results = search(hotels,loc,ind,outd,noa,noc)
for i in results:
    print "*"*20
    i[0]._hotel.show(i)
    print "*"*20
v = raw_input("end:")

