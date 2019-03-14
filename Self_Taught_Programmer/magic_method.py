#magic method->introducting repr
class Lion:
    def __init__(self,name):
        self.name=name
    def __repr__(self): # this is called when you print an object even if you dont define it
        return self.name # this method usually return the location of object on pc but we override it
lion=Lion("Dilbert")
print(lion)




#operand magic method so cool

class AlwaysPositive:
    def __init__(self, number):
        self.n=number
    def __add__(self, other):
        return abs(self.n+other.n)
x=AlwaysPositive(-20)
y=AlwaysPositive(10)
print(x+y)
# add method is called, when you have an additional operator with the objects in
#this class,python calls the method _add_on the first operand object and pass the
#second operand object into add as a paramater and returns the result
#without this you cant add obejcts or use them as operands ! reall cool! ?


