#object oriented modeling rot
class Orange:
    def __init__(self,w,c):
        """weights are in oz"""
        self.weight=w
        self.color=c
        self.mold=0# need to establish variable here when you define class then use it below?
        print("created")
    def rot(self, day, temp):#method that passes value to self.mold(
        self.mold=day*temp
orange=Orange(6, "orange")
print(orange.mold)
orange.rot(10,98)# remember call the method on the function
print(orange.mold)# print the instanc evariable value



        
