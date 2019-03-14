for i in range(4): #assigns i values from range(4) which is same as (0,1,2,3,4) and runs code until i gets assigned all of those values
    print(i)
for i in [0,1,2,3]: #same as above code
    print(i)

list(range(4)) #returns an actual list

list(range(0,100,2)) #list even values up until 100, its "skips" the odd values

supplies= ['pens', 'staplers', 'flame-trhowers', 'binders']
for i in range(len(supplies)):
    print('index'+str(i)+'in supplies is: '+supplies[i])

#multiple assignments
cat=['fat','orange','loud']
size,color,disposition=cat #this code assigns size to fat in cat, color to orange and so on and so forth
#^useful assigning multiples values from a list to a variable
