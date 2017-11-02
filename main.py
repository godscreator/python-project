import pickle
class room:
    def __init__(self):
        self._book = {} # {"year":{"month":days[]}}
        self.type = ""
        self.size = ""
    def isBookedOn(self,date,month,year):
        if self._book.has_key(year):
            if self._book[year].has_key(month):
                dts = self._book[year][month] #dates
            else:
                return False
        else:
            return False
        if date in dts:
            return True
        else:
            return False
    def isBookedIn(self,ind,outd):
        for i in range(ind[2],outd[2]+1):
            try :
                y = self._book[i]
            except KeyError:
                print "no record for mentioned year"
                return False
            for j in range(ind[1],outd[1]+1):
                m = y[j]
                for k in range(ind[0],outd[0]+1):
                    val = self.isBookedOn(k,j,i)
                    if val:
                        return True
        return False
            
    def book(self,ind,outd): #  ind = check in date , outd = check out date
         if self.isBookedIn(ind,outd) == False:
             for i in range(ind[2],outd[2]+1):
                for j in range(ind[1],outd[1]+1):
                    for k in range(ind[0],outd[0]+1):
                        if  self._book.has_key(i):
                            a = self._book[i]
                            if a.has_key(j):
                                a[j].append(k)
                            else:
                                a[j] = [k]
                        else:
                            self._book[i] = {j:[]}
             return True
         else:
            return False
    def input(self):
        for i in self.__dict__:
            if i[0] != "_":
                self.__dict__ [i] = raw_input(i+" :  ")
    def show(self , spare):
        for i in self.__dict__:
            if i[0] != "_":
               t = str(i)+" : "
               print (spare-len(t))*" " + t + str(self.__dict__[i])

f = open("good.dat","wb")
m = room()
m.input()
pickle.dump(m,f)
f.close()
f = open("good.dat","rb")
m=pickle.load(f)
m.show(20)
f.close()

