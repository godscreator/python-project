import pickle
import register
class room:
    def __init__(self):
        self._book = register.log(2000,2200)
        self.type = ""
        self.size = ""   
    def book(self,ind,outd): #  ind = check in date , outd = check out date
         if self._book.getIn(ind,outd) == False:
             self._book.setIn(ind,outd,True)
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




