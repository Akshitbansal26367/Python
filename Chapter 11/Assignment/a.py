import pickle

file_name = 'employees.dat'

# Load existing records from the binary file (if any)
try:
    with open(file_name, 'rb') as f:
        employees = pickle.load(f)
except (FileNotFoundError, EOFError):
    employees = []

while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        emp_code = input("Enter employee code: ")
        emp_name = input("Enter employee name: ")
        emp_salary = float(input("Enter employee salary: "))

        # Add the new employee record to the list
        employees.append([emp_code, emp_name, emp_salary])

        # Save the updated list to the binary file
        with open(file_name, 'wb') as f:
            pickle.dump(employees, f)
        print("Employee added successfully!")

    elif choice == '2':
        if employees:
            print("\nEmployee Records:")
            for emp in employees:
                print(f"Code: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
        else:
            print("No records found.")

    elif choice == '3':
        search_code = input("Enter employee code to search: ")
        found = False

        for emp in employees:
            if emp[0] == search_code:
                print("\nEmployee found:")
                print(f"Code: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please try again.")
