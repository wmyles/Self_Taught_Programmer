"""cracking the coding interview prob 3.2"""
"""implement push pop min with O(1)"""

#we are going to create stack(implement it)
class Stack:
    def __init__(self):
        self.items=[] # going to use a list to help implement this
        self.min_values=[]#stack to keep track of min
        
    def isEmpty(self):
        return self.items==[]# return this boolean value # as no modification is done
    
    def push(self, item):
        self.items.append(item)
        if self.min==[]:
            self.min.append(item)
        else:
            if item<self.min[len(self.min)-1]:
                self.min.append(item)
            else:
                pass
            
    def pop(self):
        self.items.pop()
        
    def getMin(self):
        return self.min[len(self.min)-1]
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1] # need to get last index(top of stack) run len -1 then index list
    
stack1=Stack()
stack1.push(2)
stack1.push(-1)
stack1.push(3)
stack1.push(1)
stack1.push(0)
print(stack1.getMin())

#test case
print(stack1.getMin()==-1)
