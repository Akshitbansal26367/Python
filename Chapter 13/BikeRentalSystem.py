"""
1. Display Available Bikes
2. Request a bike for rent (100 Rs for 1 qty)
3. Exit
"""

print("Enter 1 to display available stock of bikes")
print("Enter 2 to rent a bike (1qty = 100Rs)")
print("Enter 3 to exit from the program")


class Bike:
    __stock_quantity = 100

    def display_available_bikes(self):
        print(f"Available bikes are now {self.__stock_quantity}")

    def rent_bike(self):
        rented = int(input("Enter the quantity you like you rent : "))
        if rented <= self.__stock_quantity:
            total_cost = 100 * rented
            print(f"Congrats! {rented} bikes(s) has been rented for Rs {total_cost}")
            self.__stock_quantity -= rented
            return total_cost
        else:
            print("Not enough stock. ", end="")
            return 0


obj = Bike()
total_cst = 0
print("\n")

while True:
    choice = int(input("\nEnter your choice between 1 and 3 (both included) : "))
    if choice == 1:
        obj.display_available_bikes()
    elif choice == 2:
        cost = obj.rent_bike()
        total_cst += cost
        obj.display_available_bikes()
    elif choice == 3:
        print(f"Exiting the program. Your total cost is {total_cst}. Have a nice day!!!")
        break
    else:
        print("Please enter a valid number between 1 and 3 (both included)")
