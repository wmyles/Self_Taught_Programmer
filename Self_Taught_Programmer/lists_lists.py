#lists in lists!
lists=[]
rap=["kanye West", "Jay Z",
     "Eminem", "Nas"]

rock=["Bob Dylan",
      "The Beatles",
      "Led Zeppelin"]

djs=["zeds dead", "tiesto"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)
rap=lists[0]
rap.append("kendrick Lamar")
print(rap)
print(lists)
