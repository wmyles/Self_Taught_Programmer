#chapter 7 notes
# print each item in the following list
horror=["the walking dead", "entourage", "the sopranos", "the vampire diaries"]
for tv_shows in horror:
    print(tv_shows)
#print all the numbers from 25 to 50
for i in range(25,51):
    print(i)
#print each item in the ist from the first challenge and their indexes
for i, tv_shows in enumerate(horror):
    print(tv_shows)
    print(i)
#write a program with an infinite loop (with the option type q to quit and a lst of numbers)
    #each time trhough the lop sk the user to guess a number on the list and tell them
    #whether or not they guessed correctly

numbers_on_list=[1,2,3,7,9,12]

while True:
    guess=input("enter a number or type q to quit")# input is a string number is a number
    if guess=="q": # putting this before its converted into an integer, order is important
        break
    try:#if you try to convert a string into an int with a letter it wont work so write try statement
        guess=int(guess) 
    except ValueError: # put except right after try
        print("please type a number o q to quit")
    if guess in numbers_on_list:
        print("you guesed correctly")
    else:
        print("guess again")

#multiply all the numbers in the list [8,19,148,4] with all the numbers in the list
        #[9,1,33,83]

list_1=[8,19,148,4]
list_2=[9,1,33,83]
list_3=[]
for i, product in enumerate(list_1):
    for j, product_2 in enumerate(list_2):
        #final=product*product_2
        final=product*product_2
        list_3.append(final) # append the result of product and product_2 right after they are multiplied
    #list_3.append(final)
#print(list_3)
print(list_3)
