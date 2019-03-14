#class variable example
class Rectangle():
    rec=[] # class variable #
    #defined outside  in it method because python only calls __init__method when you create an object
    

    def __init__(self,w,l):
        self.width=w
        self.len=l
        self.recs.append((self.width,self.len))
        # dont put it here because this method is called only when object is created

    def print_size(self):
        print("""{} by {}""".format(self.width,self.len))
r1=Rectangle(10, 24)
r2=Rectangle(20,40)
r3=Rectangle(100,200)
print(Rectangle.recs)
    # appending a tuple in the list->rec with the initmethod
    #whenver a new rectangle obect is created it is automaically added to the recs list
    #takeaway, share data between different objects created by a class without global variables

