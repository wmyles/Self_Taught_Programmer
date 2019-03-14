#composition
class Dog():
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner
class Person():
    def __init__(self, name):
        self.person_name=name
mick=Person("Mick Jagger")
stan=Dog("Stanley", "Bulldog", mick)
print(stan.owner.person_name)
# so you store mick inside of class dog's owner instance variable for object stan
#in order to call it yu need to call the owner instance variable and then the instace variable that the person object references
