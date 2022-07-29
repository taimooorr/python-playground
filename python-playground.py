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

#Fibonacci Series 
def fibo(n) :
    a = 0
    b = 1
    
    if n == 1 :
        print(a)
    else :
        for i in range(2,n) :
            res = a + b
            a = b
            b = res
            print(res)
fibo(10)


#Factorial Program using for loop
def fact(n) :
    f = 1
    for i in range(1,n+1) :
        f = f * i
    return f
print(fact(5))


#Recursion
import sys
sys.setrecursionlimit(2000) # in Python by defualt recursion limit is 1000 we can change limit like this
def factRe(n) :
    if n == 1 :
        return 1
    else :
        return n * fact(n-1)
print(factRe(5))


#Lambda Function/annonymous function
#Function without name
#Syntax : lambda arguments : expression

#Example 1
x = lambda a : a + 10
print(x(5))
#example 2
b = lambda a,b : a+b

print(b(5,6))