# del() function removes an item at an index position and doesn't return it
# pop() function removes an item at an index position and returns it
# remove() function removes the specified item. If there are more than one item with the specified value, this function
# removes the first occurrence
# clear() function removes all items from the list making it an empty/null list.
# insert() function inserts an item at specified index in a list
# append() function appends an element to the end of the list
# extend() function adds items on list, tuple, dictionary etc. at the end of a list
l1 = [20, 30, 50, 60]
print("Initial list is", l1)

"""del l1[1]
print("After del() function new list is", l1)  # l1 = [20, 50, 60] """

"""print("The popped item is", l1.pop(2))
print("After pop() function new list is", l1)  # l1 = [20, 30, 60] """

"""l1.remove(50)
print("After remove() function new list is", l1)  # l1 = [20, 30, 60] """

"""l1.clear()
print("After clear() function new list is", l1)  # l1 = [] """

"""l1[0] = 90
print("The updated list is", l1)  # l1 = [90, 30, 50, 60] """

"""l1.insert(2, 70)
print("The new list is", l1)  # l1 = [20, 30, 70, 50, 60] """

n = [50, 60]
"""l1.append(n)
print("The new list is", l1)  # l1 = [20, 30, 50, 60, [50, 60]] """

"""l1.extend(n)
print("The new list is", l1)  # l1 = [20, 30, 50, 60, 50, 60] """
