# A module is a file containing a set of functions you want to include in your application
# To create a module just save the code you want in a file with the file extension .py
# We can use the module created, by using the import statement
# When using a function from a module, use the syntax: module_name.function_name.
import calc_module

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))
print("\nSum of", num1, "and", num2, "is", calc_module.sum_num(num1, num2))
print("Difference of", num1, "and", num2, "is", calc_module.sub_num(num1, num2))
print("Division of", num1, "and", num2, "is", calc_module.div_num(num1, num2))
print("Multiplication of", num1, "and", num2, "is", calc_module.mul_num(num1, num2))

'''from calc_module import print_name

s = input("\n\nEnter the name : ")
print("The name of person is", print_name(s))'''
