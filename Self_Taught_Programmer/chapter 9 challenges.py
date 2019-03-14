#Chapter 9 files excercise
"find a file on your computer and print its content using python"
import os
os.path.join("Users", "Westley", "Documents", "SAT scores by state.csv")

import csv
with open("SAT scores by state.csv", "r",encoding = "ISO-8859-1") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))
        
# had an encoding error os had to google that above

#write a program that aska s uer a question and saves answr to a file

answer=input("How Tall are you?")
with open("chapter9_question_2", "w") as f:
    f.write(answer)


# take the items in this list of list write into a csv, each list should be arow

classic_movies=[["Top Gun", "Risky Business", "Miority Report"],
                ["Titanic", "The Revenant", "Inception"],
                ["Training Day", "Man on Fire", "Flight"]]
with open("Movies.CSV", "w", newline='') as y:
    w=csv.writer(y,delimiter=",") 
    w.writerow(classic_movies[0])
    w.writerow(classic_movies[1])
    w.writerow(classic_movies[2])

        
