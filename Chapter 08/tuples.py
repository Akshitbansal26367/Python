# Tuples are used to store multiple items in a single variable
# Tuple items are ordered, unchangeable, and allow duplicate values
# Tuples are written with round brackets ()
# max() function returns the maximum element in the tuple
# min() function returns the minimum element in the tuple
# count() function returns the number of times a particular value appears in the tuple
# index() function finds the first occurrence of the specified value
# sum() function adds all items in a tuple, and return the result
t = (20, 30, 40, 50, 5, 42, 5, 5)
print("The type is", type(t))
print("Tuple element is", t[2])

# Single item cannot be stored in the tuple
'''t1 = ("Python")
print("Type of variable t1 is", type(t1))  output = <class 'str'>'''

# Tuple iteration
'''print("Tuple elements are", end=" ")
for a in range(len(t)):
    print(t[a], end=" ")'''

'''print("Tuple elements are", end=" ")
for a in t:
    print(a, end=" ")'''
print("Maximum element is", max(t))
print("Minimum element is", min(t))
print("Number of times 5 appeared in tuple is", t.count(5))
print("The first occurrence of 5 is at index", t.index(5))
print("Sum of tuple elements are", sum(t))
