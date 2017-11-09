def menu(options = {} , head = "" , chprint = "Enter your choice : ", align = 0,start = 1,back ={}):
    print "\n"+(align-len(head))*" "+head+"\n"
    l = []
    for i in back:
        print align*" "+str(len(l)+start)+"."+str(i)
        l.append(back[i])
    for i in options:
        print align*" "+str(len(l)+start)+"."+str(i)
        l.append(options[i])
    def inloop():
        try:
            v = int(raw_input("\n"+(align-len(chprint))*" "+chprint))
            print
            if v>=start and v<start+len(l):
                return v
            else:
                print "\n"+" "*align+"Error : No such option exists.\n"
                return "False"
        except ValueError:
            print "\n"+" "*align+"Error: Please enter a number\n"
            return "False"
    v = infinite(inloop,br = "False")  
    return l[v-start]

def neoInput(prompt = "", options = {} ,cmdop = "--o",help = "", cmdhl = "--h"  ,align = 0 , notnull = False):
    r = raw_input((align - len(prompt))*" " + prompt)
    if r==cmdop :
        if len(options) > 0:
            v = menu(options," Options available:  ","Enter option no.  :  ",align,start = 0,back={"back":"--b"})
            if v == "--b":
                return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull)
            else:
                return v
        else:
            print "\n"+" "*align+"Error: no options available.\n"
            return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull)
    elif r == cmdhl:
        if len(help) >0:
            print "Help:",help
        else:
            print "\n"+" "*align+"Error: no help available.\n"
        return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull)
    elif r=="" and notnull:
        print "\n"+" "*align+"Error: value cannot be null.\n"
        return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull)
    else:
        return r

def neoPrint(prompt,align =0):
    print (align - len(prompt))*" "+prompt,

def infinite(func,prompt = "",br = False):
    while True:
        f = func()
        if f != br:
            break
        elif prompt:
            print prompt
    return f
