#Chapter 4 Notes

#The List Data Type
    #A list is a value that contains multiple values in an ordered sequence
    #List value refers to the list itself
    #list value looks like this: ['cat', 'bat', 'rat', 'elephant']
    #list begins with an opening square bracket and ends with a closing square bracket
    #values inside list are called items
    #the value [ ] is an empty list like ' ' being empty string
#index=value in a given list

#Getting individual values in a list with indexes
    #say you have list ['cat','dog', etc] stored in spam
    #spam[0] would evaluate to cat
    #first value in the list is at index 0
    #python gives an IndexError error message if you use index that exceeds number of value in list
    #lists can contain other list values like spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
    #so you would need two brackets spam[0][0] would print cat

#negative indexes
    #[-1] for example, refers to the last index in a list and [-2] the second to last

#Getting sublists with slices
    # a slice can get several values from a list
    #for example, spam[1:4], a slice, will start at the first integer and goes up to be not include the value at second index

#getting a list's length with len()
    #if you store a list in a variable use len(variable name to count number of values in a list value

#Changing values in a list with indexes
        #for example if you do spam[1]=aardvark then you assign the value at index 1 the string aardvark

# List Concatenation and List Replication
    #use + to combine two lists and use * to replicate

#use del to remove values from list
    #for example del spam[2] removes value at index 2

#Working with Lists
    #creating many individual variables to store a group of similar values is bad coding
    #^ due to fact that it has a lot of duplication and your code won't be able to store more values than you have variables

#example of bad code
    #print('Enter the name of cat 1:')
    #catName1 = input()
    #print('Enter the name of cat 2:')
    #catName2 = input()
    #print('Enter the name of cat 3:')
    #catName3 = input()
    #print('Enter the name of cat 4:')
    #catName4 = input()
    #print('Enter the name of cat 5:')
    #catName5 = input()
    #print('Enter the name of cat 6:')
    #catName6 = input()
    #print('The cat names are:')
    #print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
    #catName5 + ' ' + catName6)

#instead (check example code in other program

#Using for loops with lists
    #use for loops to execute a block of code a certain number of times

#the in and not in Operators
    #use in and not in  to see if a value is in list

#the multiple assignment trick
    #multiple assignment is a shortcut that lets you assign multiple variables with the values in a list in one line of code
#augmented assignment operators
    #allows you to do math operations to variables(shortcut) see example in code and it can do the same for subtraction division etc

#Methods
#method is the same thing as a function, except it is "called on" a value

#Finding a value in a list with the index() Method
    #if value is in list(example in the code) then it returns the index of that value

#adding values to lists with the append() and insert() methods
    #append() method call adds the argument to the end of a list
    #insert() puts it in a specific place of a given list
    #as always check example code
    #important to note that these methods(all methods discussed) do not gives the new value of a variable its return variable so do not define it as a new variable!
    #^so dont do like spam=spam.append() for example wont work

#removing values from lists with remove()
    #the remove() method is passed the value to be from from a selected list
    #differs from del() because it deletes the index not the value

#sorting the values in a list with sort
    #check code on this( it sorts to an ordered list(numeric or alphabetical), can't do both integers and strings, and prioritizes uppercase over lowercase

#List-Like Types: Strings and Tuples
    #lists aren't only data types that represent ordered sequence of values
    #see example code

#Mutable and Immutable Data Types
    #lists and strings are differeint in an important way
    #lists are mutable(can be changed) strings are(immutable) cannot be changed

#Tuple Data Type
    #identical to list data type except in two ways
    #1. tuples are typed with parentheses instead of square brackets
    #2.like strings cannot be modified
    #make sure to leave a comma if you have a one value tuple
    #you can use tuples to ensure an ordered sequence of values that never change

#Converting Types with the list() and tuple() functions
    #list() and tuple() will return list and tuple values!

#References
    #when you assign a list to a variable, you are actually assigning a list reference to the variable
    #reference= value that points to some bit of data
    #list reference=value that points to a list
    #see example code, pretty cool and important explanation
    #variables contain references to list, they don't contain them

#passing references
    #References are particularly important for understanding how arguments get passed to functions. When a function is called,
     #the values of the arguments are copied to the parameter variables. For lists,
     #this means a copy of the reference is used for the parameter.

#The copy Module’s copy() and deepcopy() Functions
    #passing around references makes dealing with lists easy BUT
    #YOU may not want changes to the original list or value
    #you can use copy.copy() to make a mutable copy of the LIST not reference
    #if you have lists in lists use deepcopy()
