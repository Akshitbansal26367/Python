class DemoClass:
    a = 10

    # Constructor
    def __init__(self):
        print("Hello, I am Constructor!!!")

    def show_value(self):
        c = self.a * self.a
        print("Value is", c)

    @staticmethod
    def return_sum(a, b):
        return a + b


obj = DemoClass()
obj.show_value()
print("Sum of two numbers is", obj.return_sum(2, 30))
