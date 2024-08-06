# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.
# Python has several modes such as Read(r), Write(w), Append(a), Read and Write(r+), Write and Read(w+), Append
# and Read(a+)

# The open() function takes two parameters; filename, and mode.
f = open("test.txt", "r")

# The read() method returns the whole text
print(f.read())

'''this read(3) method will return 3 characters of the file test.txt
print("First 3 characters are " + f.read(3))
print("Characters from 4 to 7 are " + f.read(4))'''

'''You can return one line by using the readline() method
print(f.readline())
print(f.readline())
print(f.readline())

for i in f:
    print(i, end="")'''

'''The readlines() method returns a list containing each line in the file as a list item.
#print("lst = ", f.readlines())

for i in f.readlines():
    print(i)'''
f.close()
