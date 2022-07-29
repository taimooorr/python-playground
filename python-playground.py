#Global KeyWord
a = 10
def glo() :
    global a
    a = 20
    print(a)

def tryGlobals() :
    a = 30
    b = globals()['a']
    print(b)
    print(a)
    #lets try to change the global variable inside function
    globals()['a'] =40
    print(b)
tryGlobals()
