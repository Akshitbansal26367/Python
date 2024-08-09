# The pickle module is used for implementing binary protocols for serializing and de-serializing a Python object
# structure.
import pickle

# You can pickle objects with following data types : Booleans, Integers, Floats, Complex Numbers, Strings, Tuples,
# List, Sets and Dictionaries

# Python pickle module has 2 main functions dump() and load()

# dump() function is called to serialize an object hierarchy.
# load() function is called to de-serialize a data stream.

# Syntax of dump() is as follows -: dump(obj,file)
# load() function takes a file object, reconstruct the objects from the pickle representation and returns it

lst = [10, 20, 30, 40, 50]
with open('writeData.txt', 'wb') as f:  # open the file in binary write mode and dump the list
    pickle.dump(lst, f)  # use of dump() function

with open('writeData.txt', 'rb') as f1:  # open the file in binary read mode and load the list
    l1 = pickle.load(f1)  # use of load function
    print(l1)
