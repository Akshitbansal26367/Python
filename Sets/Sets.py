# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable, and unIndexed
# Sets do not allow duplicate elements.
# Sets are represented by curly braces{}
# set() function is used to convert list, tuple into set with distinct elements.
# set() function is a built-in constructor that is used to initialize a set or create an empty.
# The add() method adds an element to the set. If the element already exists, the add() method does not add the element
# The pop() method removes and returns a random element from the set.
# The remove() method removes the specified element from the set.
# The remove() method raises an error if the specified item does not exist.
# The discard() method also removes the specified element but does not raise an error if the element is not found.
# The clear() method removes all elements from a set
# The update() method updates the current set, by adding items from another set. If an item is present in both sets,
# only one appearance of this item will be present in the updated set.

s = {10, 20, 30, 10}
print("Set is", s)  # Duplicate elements are removed, so the set will be {10, 20, 30}

'''print("Set is", end='\t')
for a in s:
    print(a, end='\t')'''

'''l1 = [10, 10, 20, 30, 40, 10]
print("\nSet is", set(l1))'''

s.add(40)
print("\nNew set is", s)  # The set now includes 40

print("\nRemoved Element is", s.pop())
print("New Set is", s)  # A random element has been removed from the set

'''s.remove(20)
print("\nNew set is", s)'''

'''s.discard(20)
print("\nNew set is", s)'''

'''s.clear()
print("Empty Set is", s)'''

l1 = [20, 30, 50]
s.update(l1)
print("\nUpdated Set is", s)  # The set now includes 50, and still does not have duplicates

# Creating an empty set
harry = set()
print("\nThe empty set is", harry, "and type is", type(harry))

# Accessing elements of set
print("\nElements of set s are", end=" ")
for i in s:
    print(i, end=" ")
