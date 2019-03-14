# FOR CSV, different than before.
import csv
with open("st.csv", "w", newline='') as f:
    w=csv.writer(f,
                 delimiter=",")#storing new csv object into w with writer method
# delimiter is used to separate data
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])# writerow method twice to make two rows
    
    #remember mode, if file doesnt exit it gets created
    
