#anagram
# there is a 3 line code in which you can use sorted but wanted to build out manually
from pythonds.basic.stack import Stack
def anagram(items):
    s=Stack()
    new_items=list(items.lower())#get it in same case as characters are different
    new_compare=list(compare.lower())#get it in same case as cases are different cahrs
    for i in new_items:
        s.push(i)
    for i in range(len(s.items)):
        if new_compare[i] in new_items:
            s.pop()
    if s.isEmpty():
        is_anagram=True
    else:
        is_anagram=False
    return is_anagram


items="iceman"
compare="cinema"
print(anagram(items))


        
items="racecar"
compare="carrace"
print(anagram(items))


items="fine"
compare="dine"
print(anagram(items))



