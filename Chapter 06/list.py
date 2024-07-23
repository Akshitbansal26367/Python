# Lists are used to store multiple items in a single variable
# Lists are mutable
# Lists are created using square brackets

l1 = [1, 2, 3, 4, 5]  # Integer List
print("The list is", l1, "and its type is", type(l1))

l2 = [1, 2, 3, [4, 5, 6]]  # Nested List
print("The value is", l2[3])  # [4, 5, 6]
print("The value is", l2[3][1])  # 5

l3 = [2, 3, "Hello", [3, 4, 5]]
print(l3[2])  # Hello
print(l3[0:2])  # [2,3]
print(l3[1:])  # [3,"Hello",[3,4,5]]

l4 = [1, 2, 3, 4, 5, 6]
print(l4[0:len(l4):2])  # [1,3,5]
print(l4[len(l4):: -1])  # [6,5,4,3,2,1]
