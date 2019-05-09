"""j-> represents types of stones that are jewels
    s->represents stones i ahve
    see how many jewels we have
    J and s are strings
    chars in J are distinct
    """

def findJewels(j,s):
    count=0
    for i in range(len(s)):
        if s[i] in j:
            count+=1
        else:
            pass
    return count

#testing
#this should be 3
print(findJewels("aA", "aAAbbbb")==3)

#testing case, should be 0
print(findJewels("z", "ZZ")==0)


"""
did not use set as we need to include duplicates in counts,
maybe use a dictionary for faster membership checks,
i feel as if big o is O(n) as you need to go through string...."""
