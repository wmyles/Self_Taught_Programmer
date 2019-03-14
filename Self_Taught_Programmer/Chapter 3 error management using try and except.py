def div42by(divideBy):
    try:
        return 42/divideBy
    except:
        print('error: you tried to divide by zero.') #the try and except code here allows program to run even though an error occurs
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


print('how many cats do you have?')
numCats=input()
try:
    if int(numCats) >=4: #remember input returns a string function we need an integer to compare it to 4
        print('gee, that is a lot of cats')
    elif int(numCats) <0:
        print('you cant have negative cats, silly')
    else:
        print('not that many cats bro')
except ValueError: #this is needed because the input needs to be a numeric digit python can't make "six" into an integer but it can make "6" into one
    #example of input validation, doesn't crash the program because of improper input
    print('You did not enter a number')
