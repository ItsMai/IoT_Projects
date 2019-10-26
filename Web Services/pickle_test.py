import pickle

notes = []

# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
with open(self, 'rb') as f:
	data = pickle.load(f)
	print("sppoky\n")
# B. Print out notes

# C. Read in a string from the user using input() and append it to notes

# D. Save notes to notes.pickle

# dump information to that file
# Simple class representing a record in our database.


# class Boo:
#     def __init__(self, s):
#         self.s = s
#     def __repr__(self):
#         return "Thing: %s" % self.s
#     def save(self, notes):
#         """Save thing to a file."""
#         f = file(notes,"w")
#         pickle.dump(self,f)
#         f.close()
#     def load(notes):
#         """Return a thing loaded from a file."""
#         f = file(notes,"r")
#         obj = pickle.load(f)
#         f.close()
#         return obj
#     # make load a static method
#     load = staticmethod(load)

# if __name__ == "__main__":
#     # code for standalone use
#     foo = Boo("notes")
#     foo.save("notes.pickle")