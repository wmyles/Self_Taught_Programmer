#biggest number in a list of n integers
#assume that list is unsorted

def highest(alist):
    high_num=alist[0]
    for i in range(len(alist)-1):
        if high_num<alist[i+1]:
            high_num=alist[i+1]
    return high_num

alist=[11,33,9,18,30,7,53,5,22]

print(highest(alist))
        

alist=[44,33,9,22,30,7,53,94,22]

print(highest(alist))


alist=[33,33,9,104,30,7,53,94,22,10,12,0]

print(highest(alist))
