# Program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 both included
print("The numbers are : ", end=" ")
for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")
