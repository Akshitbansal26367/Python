# Program to get the maximum and minimum value in dictionary
d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 4, 6: 0}
max_element = d[1]
min_element = d[1]

for i in d.values():
    if i > max_element:
        max_element = i
    elif i < min_element:
        min_element = i
print("Maximum element is", max_element)
print("Minimum element is", min_element)
