# union() function return a set that contains all items from both sets, duplicates are excluded
# intersection() method returns a set that contains the similarity between two or more sets.
# difference() of the set B from set A (A - B) is a set of elements that are only in set A but not in set B
# symmetric_difference() method returns a set that contains all items from both set, but not the items that are present
# in both sets.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Union of Set A and Set B is", A | B)
# print("Union of Set A and Set B is", A.union(B))
print("Intersection of Set A and Set B is", A & B)
# print("Intersection of Set A and Set B is", A.intersection(B))
print("The set difference of Set A and Set B is", A - B)
# print("The set difference of Set A and Set B is", A.difference(B))
print("The symmetric set difference of Set A and Set B is", A ^ B)
# print("The symmetric set difference of Set A and Set B is", A.symmetric_difference(B))
