# Program to sum all items in a dictionary
d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Dictionary is", d)
sum_element = 0

for i in d:
    sum_element += d[i]
print("Sum is", sum_element)
