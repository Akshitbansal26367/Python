# The randint() method returns an integer number selected element from the specified range.
import random

# Return a number between 3 and 9 (both included)
print("Random number between 3 and 9 (both included) is", random.randint(3, 9))

# Return a number between 3 (included) and 9 (not included)
print("Random number between 3 (included) and 9 (not included) is", random.randrange(3, 9))

# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
lst = ["apple", "banana", "cherry"]
print("The random choice from list is", random.choice(lst))

# The random() method returns a random floating number between 0 and 1
print("The random floating number between 0 and 1 is", random.random())

# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
lst1 = ['badminton', 'tennis', 'archery', 'football']
random.shuffle(lst1)
print("The shuffled list is", lst1)

# The uniform() method returns a random floating number between the two specified numbers (both included).
print("The random floating number between 20 and 60 is", random.uniform(20, 60))
