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

# passing list to Fuction
def passList(lst) :
    odd = 0
    even = 0
    for i in lst :
        if i % 2 == 0 :
            even += 1
        else :
            odd += 1
    return odd, even

lst = [1,2,3,4,5,6,7,8,9,10]

even,odd = passList(lst)
print("Even : {} and Odd : {}".format(even,odd))