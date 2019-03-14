#store tuple in a list
locations=[]
la=(34.0522, 188.2437)
chicago=(41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)


#lists in a tuple
eights=["Edgar Allen poe", "Charles Dickens"]
nines=["hemmingway", "fitzgerald",
       "Orwell"]

authors=(eights,nines) #storing the list in the tuple author

print(authors)
#dictionary in a list
bday={"Hemmingway":
      "7.21.1899",
      "Fitzgerald":
      "9.24.1896"}

my_list=[bday]
print(my_list)
my_tuple=(bday,)
print(my_tuple)


# a list tuple or dictionary can be a VALUE(limitations on key they have to be immutable) in a dictationy
ny={"location":
    (40.7128, 74.0059),
    "Celebs":
    ["W.Allen",
     "Jay Z",
     "Kevin Bacon"],
    "facts":{"state":"NY","Country": "America"}
    }
print(ny)
