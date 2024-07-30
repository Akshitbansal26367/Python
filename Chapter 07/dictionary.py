# Dictionaries are used to store data values in key:value pairs
# Dictionary is a collection which is unordered, changeable and do not allow duplicates
# Dictionary is written with curly brackets {}

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("The brand of car is", thisDict['brand'])
print("The model of car is", thisDict['model'])
print("The manufacturing year of car is", thisDict['year'])

print()
print("Dictionary is", thisDict, "and its type is", type(thisDict))  # Printing Dictionary
print()
for i in thisDict:
    print("The key is", i)  # Prints the key
    print("The value is", thisDict[i])  # Prints the value
    print()
