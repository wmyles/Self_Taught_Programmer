for i in range(4): #assigns i values from range(4) which is same as (0,1,2,3,4) and runs code until i gets assigned all of those values
    print(i)
for i in [0,1,2,3]: #same as above code
    print(i)
#run individual blocks in the shell as this is an amalgam of example codes
list(range(4)) #returns an actual list

list(range(0,100,2)) #list even values up until 100, its "skips" the odd values

supplies= ['pens', 'staplers', 'flame-trhowers', 'binders']
for i in range(len(supplies)):
    print('index'+str(i)+'in supplies is: '+supplies[i])

#multiple assignments
cat=['fat','orange','loud']
size,color,disposition=cat #this code assigns size to fat in cat, color to orange and so on and so forth
#^useful assigning multiples values from a list to a variable

'howdy' in ['hello', 'hi', 'howdy', 'heyas']#in example
'cat' not in spam #not in example
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

#augmented assignment operators
spam = 42
spam += 1# example of augmented assignment operators

#swapping variables
a='aaa'
b='bbb'
a,b=b,a

#Finding a value in a list with the index method
>>> spam = ['hello', 'hi', 'howdy', 'heyas'] #if value is in list the index is returned
>>> spam.index('hello')

>>> spam.index('heyas')

>>> spam.index('howdy howdy howdy')

#adding values to code
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose') # adds moose to end of list
>>> spam

>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken') #inserts it at the first index value
>>> spam

#removing values
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam

#sorting values
spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam

>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
#does it alphabetical order and numeric order
#to ensure it sorts in alphabetical order regardless of capitalization do this:
spam.sort(key=str.lower)

#strings acting list like
name=zophie
name[0] #this will give z

#strings aren't mutable like lists
>>> name = 'Zophie a cat' #won't work
>>> name[7] = 'the'

#how to "mutate a string properly
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12] 
>>> name

#how to actually modify the list [1,2,3]
>>> eggs = [1, 2, 3]
>>> del eggs[2]
>>> del eggs[1]
>>> del eggs[0]
>>> eggs.append(4)
>>> eggs.append(5)
>>> eggs.append(6)
>>> eggs

#example of tuple
eggs = ('hello', 42, 0.5)

#converting types with list() and tuples()
>>> tuple(['cat', 'dog', 5])
>>> list(('cat', 'dog', 5))
>>> list('hello')


#references
➊ >>> spam = [0, 1, 2, 3, 4, 5]
➋ >>> cheese = spam
➌ >>> cheese[1] = 'Hello!'
spam
cheese

#the cheese[1] makes 1 in the list become cheese for BOTH SPAM AND CHEESE
#because spam and cheese share same list!

#passing references
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
#when egg is called,a return value is not used to assign a new value to spam
#it modifies the list in place!
#remember although spam and some parameter cotain separate references they refer to same list
# important to know that python acts this way

#how to copy the list(in order to make a change) not the reference to the list
>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42
>>> spam
>>> cheese
# in this code we copied the list not the reference so spam and cheese have different list values
