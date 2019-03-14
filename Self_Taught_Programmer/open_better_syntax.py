import os
os.path.join("Users", "Westley Myles", "st.txt")

#preferred syntax for opening file and closing it automatically
with open("st.txt","w") as f:
    f.write("Hi from Python, please work")
    
