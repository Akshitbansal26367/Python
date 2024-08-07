# There are two ways to write in a file : write() and writelines()
# write() inserts the string str1 in a single line in the text file
# writelines() for a list of string elements, each string is inserted in the text file.Used to insert multiple
# strings at a single time
# when we use 'with keyword' then we do not have to close the file

# f = open("write.txt", 'w')
with open("write.txt", 'w') as f:
    f.write("Hello Everyone\n")
    f.write("Love you")

    lst = ['\nPython', " is", ' interesting', ' language']
    f.writelines(lst)
    # f.close()
