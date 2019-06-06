class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.new_queue=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.new_queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.new_queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.new_queue[0]
     

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.new_queue==[]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
queue=MyQueue()

print(queue.new_queue())
queue.push(1)
queue.push(2) 
queue.push(3)
#test case
print(queue.peek()==1)
