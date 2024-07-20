w = "wscubetech"
t = len(w)

for a in range(t):
    print("w[", a, "]", "=", w[a])
print()
for i in range(t - 1, -1, -1):
    print("w[", i, "]", "=", w[i])

print()
for j in w:
    print(j)
