def average(array):
    array = set(array)
    print("The set is", array)
    return sum(array) / len(array)


N = int(input("Enter size of the array : "))
print("\nEnter the list elements : ", end=" ")
arr = list(map(int, input().split()))
result = average(arr)
print("\nThe average of distinct plant height is {:.3f}".format(result))
