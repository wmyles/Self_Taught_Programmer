#chapter 5 challenge
#1 create a list of your fave musicians
Wes_Faves=["Arctic Monkeys", "Phoenix", "Strokes", "Kendrick Lamar"]
print(Wes_Faves)

#2 create a list of tuples, with each tuple containing the longitude and latitude of somewhere you visited
visited=[]
Sacramento=("38.5816° N, 121.4944° W",)
NYC=("40.7128° N, 74.0060° W",)
Murray=("36.6103° N, 88.3148° W",)
visited.append(Sacramento)
visited.append(NYC)
visited.append(Murray)
print(visited)

#3 create a dictionary height fave color fave musician
about_me={"Height":"5'9", "Color":"Red","Artist":"Arctic Monkeys"}

#write a program that lets user ask about the dictionary and guess if its in there
guess=input("westley's Favoite Band?: ")
if guess in about_me:
    print("correct!")
    result=about_me[guess]
    print(result)
else:
    print("you dont know me")

