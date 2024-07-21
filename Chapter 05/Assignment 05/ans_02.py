# Program to count the number of frequency of each character in string
my_string = str(input("Enter a string : "))
count = {}

for letter in my_string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
for key, value in count.items():
    print(f"{key} occurs {value} times")
