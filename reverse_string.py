#reverse a string
from pythonds.basic.stack import Stack
def reverse(astring):
    s=Stack()
    reversal=""
    x=list(astring)
    print(x)#for sanity check
    for i in x:
        s.push(i)#push to stack
    for i in range(len(s.items)):
        reversal+=s.pop()#remove items from stack and store them in reversal
    return reversal                  
astring='abcdef'
print(reverse(astring))
astring='bdrtu'
print(reverse(astring))


        
        
