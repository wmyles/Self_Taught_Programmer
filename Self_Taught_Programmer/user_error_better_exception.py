try:# if user inputs string or divide by zero potential error so we need to use try clause
    a=input("enter a number: ")
    b=input("enter one more: ")
    a=int(a)
    b=int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):# what we print if the above returns an error
    print("cannot divide by zero and has to be a number")

# a
