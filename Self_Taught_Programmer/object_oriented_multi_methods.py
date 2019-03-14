#creating multiple methods
class Rectangle():
    def __init__(self, w, l):
        self.width=w
        self.length=l
    def area(self):
        return self.width*self.length# different from mold we are returning a value not making an area variable
    def change_size(self,w,l):# changing the defined variables
        self.width=w 
        self.l=l

rectangle=Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.width)# just to see the change 
print(rectangle.area())
    
