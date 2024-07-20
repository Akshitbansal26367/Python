# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
txt1 = "Welcome to {fname:>10} {lname:^10} company".format(fname="Wscube", lname="Tech")
print(txt1)

txt2 = "My name is {0}, I'm {1}".format("John", 36)
print(txt2)

txt3 = "My name is {1}, I'm {0}".format("John", 36)
print(txt3)

txt4 = "My name is {}, I'm {}".format('John', 36)
print(txt4)
