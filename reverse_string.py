#reverse a string
#from pythonds.basic.stack import Stack
#def reverse(astring):
 #   s=Stack()
  #  reversal=""
   # x=list(astring)
    #print(x)#for sanity check
    #for i in x:
     #   s.push(i)#push to stack
    #for i in range(len(s.items)):
     #   reversal+=s.pop()#remove items from stack and store them in reversal
    #return reversal                  
#astring='abcdef'
#print(reverse(astring))
#astring='bdrtu'
#print(reverse(astring))


#assume a user provides a string 
def reverse_string():
    string=input("string please")
    list_string=list(string)
    if len(list_string)==0:
        print("please give a word")
    elif len(list_string)==1:
        print(list_string)
        print("longer word please")
    elif len(list_string)>1:
        a=0
        z=len(list_string)-1
        while a<len(list_string):
            list_string[a],list_string[z]=list_string[z],list_string[a]
            a=a+1
            z=z-1
            if a>=z:
                return list_string
    else:
        print("try again")
print(reverse_string())

        
        
