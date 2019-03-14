#chapter 13 object oriented programming
#1 create rectangle and square classes classes with a method called calculate perimter that calculates
#perim of hte shapes they repsrent.

class Shapes():
    def __init__(self,w,l):
        self.width=w
        self.length=l

    def calculate(self):
        return self.width*self.length
class Rectangle(Shapes):
    pass
class Square(Shapes):
    pass

square_1=Square(20,20)
rectangle_1=Rectangle(20,40)

print(square_1.calculate())
print(rectangle_1.calculate())

#^thats inheritance in action!
#3 composition example model a rider who has a horse

class Horse():
    def __init__(self,name):
        self.name=name

class Rider():
    def __init__(self, rider_name,h):
        self.rider_name=rider_name
        self.horse_name=h

harrythehorse=Horse("Harry")
barry=Rider("Barry", harrythehorse)
print(barry.horse_name.name)
