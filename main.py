from hotel import *
def search(loc,ind,outd,noa,noc,hotels):
    for i in hotels :
        if i.location == loc :
            for j in i._rooms:
                if j._book.getIn(ind,outd) == False:
                    
