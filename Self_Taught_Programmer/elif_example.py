print('hello what is your name')
name= input()
print('how old are ya')
age=int(input()) #input is a string hence it needs to be a number becaue it's being compare do a number futher down
if name=='Alice':
    print('Hi, Alice')
   #not good code elif doesnt let you put a line of code that is not anif statement 
elif age > 2000: #remember el if only checked if the prior was false 
      print('too old')
elif age > 100:
      print('You are not Alce, grannie')
else:
    print('age is just a numer') 
      
