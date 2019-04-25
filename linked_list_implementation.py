#linked list implementation to remove middle node
#need to create these nodes have reference to data and next node, how lists are linekd
#since we are following a trail of nodes whats needed explicitly is first node
class node:# nodes need two items, its own data->ref to next list
    def __init__(self, owndata):
        self.own=owndata
        self.next_node=None#we do not know next value yet
    def getData(self): # need to access the nodes own object
        return self.own
    def getNext(self): #return value of next node
        return self.next_node
    def setData(self,newdata):#change the node value, if needed
        self.data=newdata
    def setNext(self, newnextdata):# modify next node
        self.next_node=newnextdata
        
#now we make list class
#since nodes are connections assuming list is unordered if you know first node we can find every other item
        
class unorderd_linked_list:
    def __init__(self):
        self.head=None # we dont know what this value is right now
    def isEmpty(self): # if no header then list is blank
        self.head==None
    def add_item(self,new_element):# easiest to add value to top at list
        #elements of list are stored in nodes so we pull in the nodes
        temp=node(new_element)#need to add value to node
        temp.setNext(self.head)#change next ref of new node to refer to old first node of list
        self.head=temp#set head of list  equal to new node
    def size(self):# start at head of list and count through
        current=self.head
        count=0
        while current!=None:#last node will have no value so none
            count=count+1
            current=current.getNext()
        return count
    def search(self, find_value):
        current=self.head
        found=False #not at top of list so assume false remembers if we have it
        while current!=None and not found:#
            if current.getData()==find_value:
                found=True
            else:#keep searching
                current=current.getNext()

    
    def delete(self, delete_value):# traversal needed and 
        current=self.head# start with ref set to head of list 
        previous=None# previous will be behind current(so if we start at first it will be None
        found=False# we assume item is present so we use this boolean in loop
        while current!=None and not found:
            if current.getData()==delete_value:# node has value to delete
                found=True# break out of loop
            else:# if value not found go into the next item on list
                previous=current# move previous to current
                current=current.getNext()#current is now the next node
        if previous==None:# this will be when current is the beginning item
                self.head=current.getNext()
        else:#leap frog over the item to be deelted
            previous.setNext(current.getNext())#set previous to current's next. skipping currets node thereby deleting it
    def delete_mid(self):#assumption that it isnt empty or less than two items
        midpoint=mylist.size()//2#get middle of linked list divide size by 2
        if (mylist.size())%2==0:
            print("we need odd number list")# no midpoint of even list 
        else:   
            count_index=0#get some sort of number to track pos in list
            current=self.head
            previous=None
            while current!=None:#crawl through list
                previous=current
                current=current.getNext()
                count_index=count_index+1
                if count_index==midpoint:#if index is equal to middle of the list
                    previous.setNext(current.getNext())#leap frog over current and link it to next
def show_elements():
    node=mylist.head
    while node:
        print(node.own)#node value in node class
        node = node.next_node #set to next node this will provide "iteration"


mylist = unorderd_linked_list()

mylist.add_item(31)
mylist.add_item(77)
mylist.add_item(17)
mylist.add_item(93)
mylist.add_item(26)
mylist.add_item(54)
mylist.add_item(0)
print(mylist.size())
mylist.delete_mid()
print(mylist.size())
print(show_elements())



#delete middle node so size should decreae by 1
