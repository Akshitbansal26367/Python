# function to find the max of three numbers
def find_max_three(a, b, c):
    if a > b and a > c:
        print(a, "is maximum")
    elif b > a and b > c:
        print(b, "is maximum")
    elif c > a and c > b:
        print(c, "is maximum")
    else:
        print("all three all equal")


# function to sum all the elements of the list
def sum_list_elements(lst):
    sum_element = 0
    for i in lst:
        sum_element += i
    return sum_element


# function to reverse a string
def reverse_string(string1):
    rev = ""
    for i in range(0, len(string1)):
        rev += string1[len(string1) - i - 1]
    return rev


find_max_three(12, 5, 6)
find_max_three(8, 9, 2)
find_max_three(1, 1, 6)
find_max_three(6, 6, 6)
print("The sum of all elements of list is", sum_list_elements((8, 2, 3, 0, 7)))
print("The reversed string is", reverse_string("1234abcd"))
