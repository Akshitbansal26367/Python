# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable, and unIndexed
# Sets has no duplicate elements
# Sets are represented by {}
# set() function is used to convert list, tuple into set with distinct elements.
# set() function is a built-in constructor that is used to initialize a set or create an empty.
# The add() method adds an element to the set. If the element already exists, the add() method does not add the element
# pop() function removes any random element from the set and returns the removed element.
# The remove() method removes the specified element from the set.
# remove() method is different from the discard() method, because the remove() method will raise an error if the
# specified item does not exist, and the discard() method will not
# The clear() method removes all elements in a set
# The update() method updates the current set, by adding items from another set. If an item is present in both sets,
# only one appearance of this item will be present in the updated set.
s = {10, 20, 30, 10}
print("Set is", s)
'''print("Set is", end='\t')
for a in s:
    print(a, end='\t')'''

'''l1 = [10, 10, 20, 30, 40, 10]
print("\nSet is", set(l1))'''

s.add(40)
print("\nNew set is", s)

print("\nRemoved Element is", s.pop())
print("New Set is", s)

'''s.remove(20)
print("\nNew set is", s)'''

'''s.discard(20)
print("\nNew set is", s)'''

'''s.clear()
print("Empty Set is", s)'''

l1 = [20, 30, 50]
s.update(l1)
print("\nUpdated Set is", s)
