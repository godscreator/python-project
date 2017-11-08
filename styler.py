def menu(options = {} , head = "" , chprint = "Enter your choice : ", align = 0):
    spare = (align-len(chprint))*" "
    print spare+head
    l = []
    for i in options:
        print spare+str(len(l)+1)+"."+str(i)
        l.append(options[i])
    while True:
        try:
            v = int(raw_input(spare+chprint))
            if v>0 and v<=len(l):
                break
            else:
                print "Error : No such option exists."
        except ValueError:
            print "Error: Please enter a number"
    return l[v-1]

def neoInput(prompt = "", options = {} ,cmdop = "--o",help = "", cmdhl = "--h"  ,align = 0):
    options["back"] = "--b"
    r = raw_input((align - len(prompt))*" " + prompt)
    if r==cmdop :
        if len(options) > 0:
            v = menu(options," Options available:","Enter option no. : ",align)
            if v == "--b":
                return neoInput(prompt,options,cmdop,help,cmdhl,align)
            else:
                return v
        else:
            print "Error: no options available."
            return neoInput(prompt,options,cmdop,help,cmdhl,align)
    elif r == cmdhl:
        if len(help) >0:
            print "Help:",help
        else:
            print "Error: no help available"
        return neoInput(prompt,options,cmdop,help,cmdhl,align)
    else:
        return r

def neoPrint(prompt,align =0):
    print (align - len(prompt))*" "+prompt

def infinite(func,prompt = "",br = False):
    while True:
        f = func()
        if f == br:
            if prompt:
                print prompt
            break
v = neoInput("Enter type : ",options = {"good":"good","bad":"bad","worse":"worse"},help = "your score depends on your choice",align =0)
print "your score:",v
