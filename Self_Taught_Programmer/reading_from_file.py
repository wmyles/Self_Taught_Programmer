#st is a file i created from a previous example based on book example
import os
os.path.join("Users", "Westley Myles", "st.txt")
#once file is created not sure i need the above
with open("st.txt","r") as f:
    print(f.read())
