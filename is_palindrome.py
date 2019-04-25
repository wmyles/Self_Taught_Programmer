# palindrome
#assume a user gives a string
#in place 
def palindrome():
    string1=input("enter a string")
    list_string=list(string1)
    i=0
    j=len(list_string)-1
    is_Palindrome=True
    if len(list_string)==0:
        print("please input a word")
    if len(list_string)==1:
        print("yes technically palindrome but longer word please")
    else:
        while i<len(list_string):
            if list_string[i]==list_string[j]:
                i=i+1
                j=j-1
                if i>=j:
                    return is_Palindrome
                    print("is palindrome")
            else:
                is_Palindrome=False
                return is_Palindrome
                print("not palindrome")
print(palindrome())
            
