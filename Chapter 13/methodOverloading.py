class Area:
    @staticmethod
    def find_area(a=None, b=None):
        if a is not None and b is not None:
            print("Area of rectangle is", a * b)
        elif a is not None:
            print("Area of square is", a * a)
        else:
            print("Nothing is found")


obj = Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10, 20)
