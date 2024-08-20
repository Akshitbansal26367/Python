n = int(input("Enter the number of elements in Set A : "))
print(f"Enter {n} elements for Set A(space-separated) : ", end=" ")
setA = set(map(int, input().split()))
print(f"Set A : {setA}")

b = int(input("Enter the number of elements in Set B : "))
print(f"Enter {b} elements for Set B(space-separated) : ", end=" ")
setB = set(map(int, input().split()))
print(f"Set B : {setB}")

ans = setA | setB
print(f"\nThe union of Set A and Set B is : {ans}")
print(f"The number of unique elements in the union is : {len(ans)}")
