#file path example and then writing to it
import os
os.path.join("Users", "Westley Myles", "st.txt")

st=open("st.txt", "w") # open a file for writing only
st.write("Hi from Python!")
st.close

# above used open function to open the file and save the objec it returns in the variable st
#then use write method on st which accepts a string ond writes it to to the new file python created
#close used to close file


