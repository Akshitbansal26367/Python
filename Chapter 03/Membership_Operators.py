"""in
not in"""

w = "welcome"
n = 'z'
print(n in w)  # False

l1 = [10, 20, 30, 40]
print(40 in l1)  # True
print(50 not in l1)  # True

str1 = "welcome to wscubetech"
s = "to"
print(s in str1)  # True
if s in str1:
    print("YES")
else:
    print("NO")

l2 = [20, 30, 40, 50, 60]
v = 80

if v not in l2:
    print(v, "Not in l2 list")
else:
    print(v, "is in l2 list")
