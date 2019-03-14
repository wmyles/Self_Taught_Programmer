Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
Traceback (most recent call last):
  File "/Users/Westley/Documents/name_password.py", line 1, in <module>
    if name=='Mary':
NameError: name 'name' is not defined
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
Traceback (most recent call last):
  File "/Users/Westley/Documents/name_password.py", line 2, in <module>
    name== input()
NameError: name 'name' is not defined
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
wes
>>> 
>>> wes
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    wes
NameError: name 'wes' is not defined
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
wes
wrong password
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
Mary
hello mary
Traceback (most recent call last):
  File "/Users/Westley/Documents/name_password.py", line 5, in <module>
    if password== 'swordfish':
NameError: name 'password' is not defined
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
Mary
hello mary
what is the password
nah
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
Mary
swordfish
hello mary
what is the password
access granted
>>> 
============= RESTART: /Users/Westley/Documents/name_password.py =============
what is your name
Mary
hello mary
what is the password
swordfish
access granted
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
a
Traceback (most recent call last):
  File "/Users/Westley/Documents/elif_example.py", line 5, in <module>
    elif age>2000:
NameError: name 'age' is not defined
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
Alice
how old are you
1
Hi, Alice
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
Alice
how old are you
Hi, Alice
how old are you

============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
Alice
Hi, Alice
how old are you
2
>>> 2
2
>>> 2
2
>>> 2
2
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
alice
Traceback (most recent call last):
  File "/Users/Westley/Documents/elif_example.py", line 7, in <module>
    elif age>2000:
NameError: name 'age' is not defined
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
Alice
Hi, Alice
how old are you
30
>>> 101
101
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
Alice
Hi, Alice
how old are you
2001
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
Alice
how old are ya
Hi, Alice
>>> 10
10
>>> 10
10
>>> 10
10
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
wes
how old are ya
Traceback (most recent call last):
  File "/Users/Westley/Documents/elif_example.py", line 8, in <module>
    elif age>2000:
TypeError: '>' not supported between instances of 'builtin_function_or_method' and 'int'
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name

============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
wes
how old are ya
21
Traceback (most recent call last):
  File "/Users/Westley/Documents/elif_example.py", line 8, in <module>
    elif age>2000:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
wes
how old are ya
1
Traceback (most recent call last):
  File "/Users/Westley/Documents/elif_example.py", line 8, in <module>
    elif age > 2000:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 
============= RESTART: /Users/Westley/Documents/elif_example.py =============
hello what is your name
wes
how old are ya
2
age is just a numer
>>> 
