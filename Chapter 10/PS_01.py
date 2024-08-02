# Define a function that can accept two strings as input and print the string with maximum length. If two strings
# have the same length, then the function should print all strings line by line
# Program to find HCF of two numbers
# Program to find armstrong number in an interval
def string_accept(str1, str2):
    if len(str1) > len(str2):
        print(str1, "is of maximum length")
    elif len(str1) < len(str2):
        print(str2, "is of maximum length")
    else:
        print(str1, end=" ")
        print(str2, "are of equal length")


def hcf_answer(num1, num2):
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


def armstrong_range(num1, num2):
    for i in range(num1, num2):
        temp = i
        dig_count = 0
        while temp != 0:
            temp = temp // 10
            dig_count += 1

        temp = i
        sum_elements = 0
        while temp != 0:
            ans = pow(temp % 10, dig_count)
            sum_elements += ans
            temp = temp // 10
        if sum_elements == i:
            print(i, end=" ")


string1 = input("Enter string1 : ")
strint2 = input("Enter string2 : ")
string_accept(string1, strint2)

n1 = int(input("\nEnter num1 : "))
n2 = int(input("Enter num2 : "))
HCF_ans = hcf_answer(n1, n2)
print("HCF of", n1, "and", n2, "is", HCF_ans)

n1 = int(input("\nEnter num1 : "))
n2 = int(input("Enter num2 : "))
print("The armstrong numbers between", n1, "and", n2, "are : ", end="")
armstrong_range(n1, n2)
