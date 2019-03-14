#number 2 chapter 13
class Square():
    def __init__(self, s):
        self.side=s
    def change_size(self,s):
        self.side=s
square_1=Square(5)

print(square_1.side)
square_1.change_size(10)
print(square_1.side)

