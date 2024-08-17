# Program to read an entire text file
f = open("file.txt", 'r')
print(f.read())
f.close()

# Program to read the first n lines of the file
n = int(input("\nEnter number of lines to read : "))
with open('file.txt', 'r') as f:
    lines = f.readlines()[:n]  # Read all lines and slice the first n lines
    print(''.join(lines))
