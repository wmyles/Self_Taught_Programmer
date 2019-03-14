#Chapter 4 Challenge

#1 write a function that takes a number as an input and returns number squared
#not asking for user input
def squared(x):
    return x**2
print(squared(2))

#2 create a function that accepts a string as a param and prints it
#again not asking for user input
def your_words(y):
    print(y)
your_words("strings: stringstingstring")

 # 3 function that takes threerequired params and two optional

def fact(x,y,z, a=4, b=5): #optional params are 4 and 5, mandatory comes first
    return x+y+z+a+b

results=fact(1,2,3)
print(results)


#4 see page 66
def first(x):
    return x/2

def second(x):
    return results*4

y=first(4)
z=second(y) # pass the result of first with param here(which is y) inta z
print(z)
#5 write a function that converts a float to a string, write an exception
def convert(x):
    try:
        return float(x)
    except ValueError:
        print("cannot convert string to float")

c=convert("55.0")    
print(c)
