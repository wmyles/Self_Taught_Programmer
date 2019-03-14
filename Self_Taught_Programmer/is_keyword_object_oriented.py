class Person:
    def __init__(self):
        self.name='Bob'
bob=Person()
same_bob=bob
print(bob is same_bob)
#true because both variables ppint to the same Person Object
another_bob=Person()
print(bob is another_bob)
#should be false because another _bob creates a new person object

