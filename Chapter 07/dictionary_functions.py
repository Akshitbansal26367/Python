# The get() method returns the value of the item with the specified key
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples
# in a list.
# del keyword removes the item with the specific key name
# The pop() method removes the item with the specific key name. This method returns the deleted item
# The update() method inserts the specified items to the dictionary.
# The clear() method removes all the elements from a dictionary.
d = {
    'name': 'Python',
    'fees': 8000,
    'duration': '2months'
}

print("The fees is", d.get('fees'))
print("The keys are :", d.keys())
print("The keys are : ", end="\t")
for i in d.keys():
    print(i, end="\t")
print("\n")

print("The values are :", d.values())
print("The values are : ", end="\t")
for i in d.values():
    print(i, end="\t")
print("\n")

print("Key:Value pair are", d.items())
print("Key:Value pair are ", end=" ")
for i, j in d.items():
    print(i, ":", j, end="\t")

'''del d['fees']
print("\n\nUpdated Dictionary is", d)

d.pop('name')
print("Updated Dictionary is", d)'''

'''d['fees'] = 10000
d.update({'fees': 12000})
print("\n\nUpdated Dictionary is", d)'''

'''d.update({'tutor': 'Pradeep'})
d['tutor'] = 'pradeep'
print("\n\nUpdated Dictionary is", d)'''

'''d.clear()
print("Updated Dictionary is", d)'''
