#chapter 14 challenges
#1. add square list class variable to a class called square so
class Square:
    square_list=[]

    def __init__(self, w,l):
        self.width=w
        self.length=l
        self.square_list.append((self.width, self.length)) # makes this one argument for append?
        #append a list to the class variable(no need to set it equal to anything)
    def print_size(self):
        print("""{}, by {}, by {}, by {}""".format(self.length,self.length, self.length,self.length))
sq1=Square(10,10)
sq2=Square(20,20)
sq3=Square(30,30)

print(Square.square_list)
print(sq1.print_size())
