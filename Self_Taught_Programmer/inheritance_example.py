# inheritance
class Shape():
    def __init__(self, w,l):
        self.width=w
        self.length=l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,self.length))
my_shape=Shape(20,25)
my_shape.print_size()#the function when called prints so no need to print

#now have a class inherit it
class Square(Shape):
    pass # means do nothing, it inherits the variables and methods
    #still  need to make a square object

a_square=Square(20,20)
a_square.print_size()


#method overriding below

class Rectangle(Shape):#inherit variables etc from class shape
    def area(self):
        return self.width*self.length
    def print_size(self):
        print("""I am {} by {}""".format(self.width,self.length))
        #this uses same method as print size but see how in this child class we override it

a_rectangle=Rectangle(20,40)
print(a_rectangle.area())
a_rectangle.print_size()


