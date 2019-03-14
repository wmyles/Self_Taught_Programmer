rhymes={"1":"fun", "2":"blue",
        "3":"me", "4": "floor",
        "5":"live"
        }
n=input("type a number:")
if n in rhymes:
    rhyme=rhymes[n]
    print(rhyme)
else:
    print("not found")

#another guessing games, taking user input and seeing if it's a key in the dictionary and printing the associated value
