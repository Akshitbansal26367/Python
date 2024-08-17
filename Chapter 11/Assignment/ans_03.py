# Program to append text to a file and display the text
with open('append.txt', 'a') as f:
    f.write("\nHindi is my Mother language")
with open('append.txt', 'r') as file:
    print(file.read())
