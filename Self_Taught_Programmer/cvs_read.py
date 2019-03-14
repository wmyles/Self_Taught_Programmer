# this program works because i am using the file from CSV_example
import csv
with open("st.csv","r") as f:
    r=csv.reader(f, delimiter=",")
    for row in r:#because the object we return from the above is iterable csv object
        print(",".join(row))
        # lets test and see logic here
    # open st.csv for reading and convert it to a csv object with reader method
    # we iterate through csv object using a loop, each time around loop we call
    #the join method on a comma to add a comma between each piece of data in the file
    #to print the conetns the way they appear in the original file
    
        
