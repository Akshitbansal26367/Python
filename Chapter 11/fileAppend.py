# There are two ways to append data in a file : write() and writelines()
f = open('append.txt', 'a')
f.write('\nHello Everyone')
f.close()
