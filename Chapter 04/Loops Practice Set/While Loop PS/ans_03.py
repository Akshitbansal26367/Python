# Program that accepts sequence of lines as inputs and prints the lines after making all characters in the sentence
# capitalized
while True:
    h = input("Enter the string : ")
    if h == "":
        break
    else:
        a = h.upper()
        print("Capitalised String is :", a)
