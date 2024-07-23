# count() function returns the number of times the value appears in the list
# max() function returns the maximum value present in the list
# min() function  returns the element with minimum value in the list
# sort() function sorts the elements of a list. It sorts in ascending order by default
# reverse() function reverses the sorting order of the elements
# index() function searches for a given element from the start of the list and returns the position of the first
# occurrence.
l1 = [10, 20, 30, 50, 10]
print("The count of 10 in the list is", l1.count(10))  # 2
print("The max item in list is", max(l1))  # 50
print("The min item in list is", min(l1))  # 10
"""l1.sort()
print("The sorted list is", l1)  # l1 = [10, 10, 20, 30, 50]"""
l1.reverse()
print("The reversed string is", l1)  # l1 = [10, 50, 30, 20, 10]

l2 = ["Hello", "my", "name", "is", "Akshit", "Bansal"]
print("\nThe max item in list is", max(l2))  # name
print("The min value in list is", min(l2))  # Akshit
# l2.sort()
# print("The sorted list is", l2)  # l2 = ['Akshit', 'Bansal', 'Hello', 'is', 'my', name']
print("The index of 'is' in the list is", l2.index('is'))
