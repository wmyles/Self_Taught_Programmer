
#the use of global here allows us to change x only in this function not everywhere
x=100
def f():
    global x
    x+=1
    print(x)

f()
