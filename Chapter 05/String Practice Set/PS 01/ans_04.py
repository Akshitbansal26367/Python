# Program to reverse words in a sentence without using library method
w = str(input("Enter the string : "))
z = ""
print("The reversed string is", w[-1::-1])

print("The reversed string is ", end="")
for a in range(len(w) - 1, -1, -1):
    print(w[a], end="")

for a in w:
    z = a + z
print("\nThe reversed string is", z)
