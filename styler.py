def menu(options = {} , head = "" , chprint = "Enter your choice : ", align = 0,start = 1,order=[],select = False):
    print (align-len(head))*" "+head
    l = []
    keys = options.keys()
    for i in order:
        print align*" "+str(len(l)+start)+"."+str(i)
        l.append(options[i])
        keys.remove(i)
    for i in keys:
        print align*" "+str(len(l)+start)+"."+str(i)
        l.append(options[i])
    while True:
        k = []
        v = raw_input((align-len(chprint))*" "+chprint)
        v = v.split(",")
        if len(v)==1:
            try:
                v=int(v[0])
                if v in range(start,start+len(l)):
                    k=l[v-start]
                    break
                else:
                    print " "*align+"Error : option \""+str(v)+"\" does'nt exist."
            except ValueError:
                print " "*align+"Error: \""+str(v[0])+"\" is not a number."
                        
        elif len(v)>1:
            if select:
                for i in v:
                    try:
                        i=int(i)
                        if i not in range(start,start+len(l)):
                            print " "*align+"Error : option \""+str(i)+"\" does'nt exist."
                            break
                        else:
                            k.append(l[i-start])
                    except ValueError:
                        print " "*align+"Error: \""+str(i)+"\" is not a number."    
                        break
                else:
                    break
            else:
                print " "*align+"Error: selection of options not available."
    return k

def neoInput(prompt = "", options = {} ,cmdop = "--o",help = "", cmdhl = "--h"  ,align = 0 , notnull = False,select=False,onlyoptions=False):
    if not options:
        onlyoptions=False
    if onlyoptions :
        print (align - len(prompt))*" " + prompt
        r = cmdop
    else:
        r = raw_input((align - len(prompt))*" " + prompt)
    if r==cmdop :
        if len(options) > 0:
            options.update({"back":"--b"})
            v = menu(options," Options available:  ","Enter option no.  :  ",align,start = 0,order=["back"],select=select)
            if v == "--b" or "--b" in v:
                return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
            else:
                return v
        else:
            print "\n"+" "*align+"Error: no options available.\n"
            return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
    elif r == cmdhl:
        if len(help) >0:
            print "Help:",help
        else:
            print "\n"+" "*align+"Error: no help available.\n"
        return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
    elif r=="" and notnull:
        print "\n"+" "*align+"Error: value cannot be null.\n"
        return neoInput(prompt,options,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
    else:
        return r

def neoPrint(prompt,align =0):
    print (align - len(prompt))*" "+prompt,

