#This is a guess the number game
import random
secretNumber=random.randint(1,20)
print('I am think of a number between 1 and 20.')

#ask the player to guess 6 times

for guessesTaken in range(1,7): #this code loops at most 6 times allowing 6 guesses
    print('Take a guess.')
    guess=int(input())#remeber input returns string! need int here for numeric value

    if guess< secretNumber:
        print('Your guess is too low.')
    elif guess> secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is the correct guess!
if guess==secretNumber:
    print('Good job, you guessed my number in'+str(guessesTaken) +'guessess!')
else:
    print('Nope. The number I was thinking of was ' +str(secretNumber))
