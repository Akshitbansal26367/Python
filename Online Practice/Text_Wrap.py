# import textwrap

S = input("Enter the string : ")
max_width = int(input("Enter the value for formatting : "))

'''Method 1 using textwrap
lst = textwrap.fill(S, max_width)
print(lst)'''

ans = ""
for i in range(0, len(S), max_width):
    ans = ans + S[i:i + max_width] + "\n"
print(ans)
