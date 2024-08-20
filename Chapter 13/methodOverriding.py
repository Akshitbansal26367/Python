class A:
    def showdata(self):
        print("I am in Class A")


class B(A):
    def showdata(self):
        print("I am in Class B")
        super().showdata()


obj = B()
obj.showdata()
