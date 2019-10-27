# Names: Emily, Mailani
import pickle
import os

notes = []
# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
if not os.path.exists("notes.pickle"):
	os.mknod("notes.pickle") # create a file
file1 = open("notes.pickle","rb") # open the file in read/binary mode

try:
    notes = pickle.load(file1)
except EOFError:
    print("empty")
    notes = []
file1.close()

# B. Print out notes
for i in range(len(notes)):
	print(notes[i])

# C. Read in a string from the user using input() and append it to notes
temp = input()
notes.append(temp)

# D. Save notes to notes.pickle
file2 = open("notes.pickle","wb") # open the file in write/binary mode
pickle.dump(notes,file2)
file2.close()
