# We make private data members using (__) symbol.
# We make private data functions using (__) symbol.
class Student:
    __printName = "Hello my name"  # printName is private data member

    def __init__(self):
        self.__name = ""  # name is private data member
        print(self.__printName)
        self.__display_info()

    def get_name(self):
        return self.__name

    def set_name(self, name1):
        self.__name = name1

    @staticmethod
    def __display_info():  # display_info() is private member function
        print("Welcome to my new house")


obj = Student()
obj.set_name("Testing My Program")
print(obj.get_name())
