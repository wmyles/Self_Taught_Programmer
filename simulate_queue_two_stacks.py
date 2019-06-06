"""simulate queue with two stacks
   idea is to push items into one stack to show entrance into queue
   then pop it into the outstack so items that entered instack first
   gets popped out first
"""

class MyQueue:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()#helper function to move items into outstack before popping
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.inStack==[] and self.outStack==[]
        
    def move(self):
        """
        :rtype nothing
        """
        
        if self.outStack==[]: #ifoutstack is empty
            while self.inStack:
                self.outStack.append(self.inStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
queue=MyQueue()

queue.push(1)
queue.push(2)

"""test cases
   should be true true and true and true respectively for below code"""
print(queue.peek()==1)
print(queue.pop()==1)
print(queue.empty()==False)
