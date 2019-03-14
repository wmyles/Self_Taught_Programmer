import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return 'it is certain'
    elif answerNumber==2:
        return 'it is decidedly so'
    elif answerNumber==3:
        return 'yes'
    elif answerNumber==4:
        return 'reply hazy, try again'
    elif answerNumber==5:
        return 'ask again later'
    elif answerNumber==6:
        return 'concentrate and try again'
    elif answerNumber==7:
        return 'my reply is no'
    elif answerNumber==8:
        return 'outlook not so good'
    elif answerNumber==9:
        return 'very doubtful'

r=random.randint(1,9)
fortune=getAnswer(r)
print(fortune)#can shorten to one line print(getanswer(random.randint(1,9)))
#python imports random module
#then thegeanswr function is defined
#since not called, code is skipped
#next the random randominteger  function is called with two arguments
#evaluates to random integer which is stored in r
#getanswer function is called with r as the argument
#prgram exuection moves to the top of get answer and r is stored in the paramater named answer number
#then depending on value stored in get answer returns one of possible values
#program returns to line at bottom of prgram that orignall caleed get answer
#the returned string is assigned a variable named fortune which then gets passed to a print
