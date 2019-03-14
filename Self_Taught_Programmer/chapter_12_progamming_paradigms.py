#chapter 12 program paradigms

#1 ddefine a class called apple with four instance variables

class Apple():
    def __init__(self,c,s,t,g):
        self.color=c # you can make the params actual names doesnt have to be c
        self.size=s
        self.taste=t
        self.category=g
        print("created!")
aapl=Apple("red",10,"good","granny smith")
print(aapl)

#create a circle class with a method called area that calcualtes and returns it

import math
class Circle():
    def __init__(self,r):
        self.radius=r

    def area(self):
        return (self.radius**2)*math.pi
cir1=Circle(10)
print(cir1.area())


        
        
class Triangle():
    def __init__(self,b,h):
        self.base=b
        self.height=h

    def area(self):
        return (self.base*self.height)/2
tri=Triangle(10,20)
print(tri)
print(tri.area())

class Hexagon():# i did area should be permiter but same logic 
    def __init__(self,a):
        self.area_measure=a

    def area(self):
        return ((3*math.sqrt(3))/2)*(self.area_measure*self.area_measure)
hex=Hexagon(10)
print(hex.area())






    
