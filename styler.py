def menu(options,vals, head = "" , chprint = "Enter your choice : ", align = 0,start = 1,select = False):#options=[],vals=[]
    #   ****displaying the menu.****
    print (align-len(head))*" "+head
    for i in range(len(options)):
        print align*" "+str(i+start)+"."+options[i]
    #   ****taking input.****
    f = False # flag f denotes successful entry.
    while not f:
        try:
            v = eval(raw_input((align-len(chprint))*" "+chprint)+",")#forcefully turning inputs in tuple for easier selection.
            g = False # flag g denotes unsuccessful entry.
            for j in range(len(v)):#checking all values taken as input.
                if not (v[j]>=start and v[j]<start+len(options)):# if invalid option.
                    print " "*align+"Error : option \""+str(v[j])+"\" does'nt exist."
                    g = True
                else:
                    f = True
                if not select:# stop checking further value if select is not on.
                    break
            if g:# if unsuccessful entry then loop again.
                f = False
        except (NameError,SyntaxError):
            print align*" "+"Error: please enter a number or numbers seperated by comma."
    #   **** returning the values.****
    l = []#denote values to return.
    for i in v:
        l.append(vals[i-start])
    if select:
        return l
    else:
        return l[0]# return only one value if select is off.

def neoInput(prompt="",options=[],vals=[],cmdop="--o",help="",cmdhl="--h",align=0,notnull=False,select=False,onlyoptions=False):
    #   ****input made through options only.****
    if onlyoptions and options:
        print (align - len(prompt))*" " + prompt
        r = cmdop
    else:
        r = raw_input((align - len(prompt))*" " + prompt)
    if r==cmdop :# user opts for options for input.
        if options:
            # options menu.
            v = menu(options+["back"],vals+["--b"],"Options available : ","Enter option no : ",align,start = 0,select=select)
            if v == "--b" or "--b" in v:# if user opts for back.
                return neoInput(prompt,options,vals,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
            else:
                return v
        else:
            print "\n"+" "*align+"Error: no options available.\n"
            return neoInput(prompt,options,vals,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
    elif r == cmdhl:# user opts for help for input.
        if len(help) >0:
            print "Help:",help
        else:
            print "\n"+" "*align+"Error: no help available.\n"
        return neoInput(prompt,options,vals,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
    elif r=="" and notnull:# in case value cannot be null.
        print "\n"+" "*align+"Error: value cannot be null.\n"
        return neoInput(prompt,options,vals,cmdop,help,cmdhl,align,notnull,select,onlyoptions)
    else:#regular input
        return r

def neoPrint(prompt,align =0):
    print (align - len(prompt))*" "+prompt,

