# Program to find the second-smallest number in a list
l1 = [2, 2, 9, 7, 5, 2, 6, 3, 2, 2]
l1.sort()  # l1 = [2, 2, 2, 2, 2, 3, 5, 6, 7, 9]

smallest = l1[0]
for i in range(1, len(l1)):
    if l1[i] != smallest:
        print("Second smallest element is", l1[i])
        break
