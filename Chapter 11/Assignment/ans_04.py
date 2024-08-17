"""Write a menu driver program in Python that asks the user to add, display and search records of employees stored in
a binary file. The employee record contains employee code, name and salary. It should be stored in a list
object.
Your program should pickle the object and save it to a binary file."""

import pickle

# Employee data as list of lists
employees = [['E001', 'Alice', 50000], ['E002', "Bob", 60000], ['E003', 'Charlie', 55000]]

# Create and save the employee records to the binary file
with open('employee.txt', 'wb') as file:
    pickle.dump(employees, file)

# Load existing records from the binary file
with open('employee.txt', 'rb') as f:
    employees = pickle.load(f)

print("Press 1 to Add Employee")
print("Press 2 to Display Employees")
print("Press 3 to Search  Employee")
print("Press 4 to Exit Program")
while True:

    choice = input("\nEnter your choice : ")

    if choice == '1':
        emp_code = input("Enter the employee code  : ")
        emp_name = input("Enter the employee name  : ")
        emp_salary = int(input("Enter the employee salary : "))

        # Add the new employee record to the list
        employees.append([emp_code, emp_name, emp_salary])

        # Save the updated list to the binary file
        with open('employee.txt', 'wb') as f:
            pickle.dump(employees, f)
            print("Employee added successfully!")

    elif choice == '2':
        if employees:
            for emp in employees:
                print(f'Code : {emp[0]}, Name: {emp[1]}, Salary : {emp[2]}')
        else:
            print("No record found")

    elif choice == '3':
        search_code = input("Enter employee to search : ")
        found = False

        for emp in employees:
            if emp[0] == search_code:
                print("\nEmployee found : ", end="")
                print(f'Code : {emp[0]}, Name: {emp[1]}, Salary : {emp[2]}')
                found = True
                break

        if not found:
            print("Employee not found")

    elif choice == '4':
        print("Exit the program")
        break

    else:
        print("Invalid Choice, please try again")
