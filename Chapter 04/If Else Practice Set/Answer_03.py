# Calculate Number of digits and alphabets in the string
s = input("Enter the string : ")
digit_count = 0
alphabet_count = 0

for a in s:
    if a.isdigit():
        digit_count = digit_count + 1
    elif a.isalpha():
        alphabet_count = alphabet_count + 1
print("Total digits    :", digit_count)
print("Total alphabets :", alphabet_count)
