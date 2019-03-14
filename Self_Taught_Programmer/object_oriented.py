#object oriented programming

class Orange:
    def_init_(self):
        print("created")

class Orange:
    def_init_(self,w,c):
        self.weight=w
        self.color=c
        proint("Created!")

# above two have no object created but latter has instance variable!
# might have to comment the above two out

class Orange:
    def_init_(self,w,c):
        self.weight=w
        self.color=c
        print("created")
orl=Orange(10, "dark orange")
print(orl)
# we define the class and after words we instantiate the orange class with cpde
#orange(10,"dark orange") and Created! prints. then we print the orange object
#itslf-> leads to python telling you it is an orange obhect and gives you location
# of it in your memory


class Orange:
    def_init_(self,w,c):
        self.weight=w
        self.color=c
        print("created")
orl=Orange(10, "dark orange")
print(orl.weight)
print(orl.color)
# to print the value of instance variable, object name.variable name
#notice that we do not have tp pass in self in orl=orange(10, "dark orange)
# python does that automatically
