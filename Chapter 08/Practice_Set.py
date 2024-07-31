# Program to reverse a tuple
t = ('a', 'b', 'c', 'd', 'e')
lst = list(t)  # converts tuple into list
lst.reverse()
print("Reversed Tuple is", tuple(lst))

# Program to find the index of an item of a tuple
t1 = ('red', 'blue', 'green', 'yellow', 'orange')
print("The index of yellow is", t1.index('yellow'))

# Program to remove an item from tuple
t2 = (2, 3, 4, 5, 6, 7, 'hello')
lst = list(t2)
lst.remove(5)
print("Tuple is", tuple(lst))
