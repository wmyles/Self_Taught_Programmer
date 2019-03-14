class Orange:
    def __init__(self, w, c):
        self.weight=w
        self.color=c
        print("created!")      
orl=Orange(10,"dark orange")

print(orl)
print(orl.weight) # print value of instance variable
print(orl.color)
