#loops with lists tuples, dictionaries
shows=["GOT", "Narcos",
       "Vice"]

for show in shows: #show gets assigned item from iterable so print it!
    print(show)

coms=("A. Development", "Friends", "Always Sunny")
for comedies in coms:
    print(comedies)
people={"G. Bluth II":"A. Development", "Barney":"HIMYM", "Dennis":
        "It's Always Sunny"}
for characters in people:
    print(characters)

#use for-loops to change the item in a mutable, like a list
tv=["GOT", "Narcos", "Vice"]
i=0
for show in tv:
    new=tv[i] #iterate through tv and assign it to new
    new=new.upper() 
    tv[i]=new #assign the item at current index determined by loop into tv
    i+=1 #increase i by 1 loop will run through tv but we need to increment i!
print(tv)

# correct? syntax for the above process accessing each item and its index in an iterable
wes_tv=["Parks and Recs", "Agents of Shield", "Bird Box"]
for i, show in enumerate(wes_tv): # i is integer value 
    new=wes_tv[i] #grab ith value of wes_tv store it in new
    new=new.upper()
    wes_tv[i]=new # assign this value of new into wes_tv(we use i in wes_tv as we are replacing the uncapitalized version with the capitalized one

print(wes_tv)

#move data between iterables
tv=["GOT", "Narcos", "Vice"]
coms=["arrested development", "friends", "always sunny"]
combined=[ ]
for drama in tv:
    drama=drama.upper() #remember drama gets the index item of iterable at each loop
    combined.append(drama)
for comedies in coms:
    comedies=comedies.upper()
    combined.append(comedies)#append already modifies variable no need to assing it to itself
print(combined) 
    
# iterating throug values in i. 
for i in range(1,11):
    print(i)


#while loop
x=10
while x>0:
    print('{}'.format(x))
    x-=1
print("Happy New Year!")


#Break statement
qs=["what is your name?", "what is your fav.color?",
    "what is our quest?"]# list of questions to be asked
n=0#n is integer value)
while true:
    print("type q to quit")
    a=input(qs[n]) # ask the questions from the list(n is integer value
    if a=="q":
        break
    n=(n+1)%3 #this allows you to cycle through this forever, remainder
    #once n hits 3 3%3 has no remainder, so its 0 and this starts again 
#^indefinitely ask question until user breaks out of loop

#continue statement
for i in range(1,6):
    if i==3: # it will not print the number 3 it will skip to next iteration
        continue
    print(i)

#nested loops
for i range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:# nested loop
        print(letter)

#use two for-loops to add each number in a list to all numbers in another list
list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]
for i in list1:
    for j in list2:# this will loop through list 2 before continuing outer loop so 1+5 1+6 etc
        added.append(i+j)
print(added)
    



