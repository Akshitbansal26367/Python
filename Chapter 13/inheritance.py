"""Single Level Inheritance
class Child:
    @staticmethod
    def print_child():
        print("I am Child Class")


class Parent(Child):
    @staticmethod
    def print_parent():
        print("I am Parent Class")


Parent.print_child()
Parent.print_parent() """

"""Multilevel Inheritance
class A:
    @staticmethod
    def print_a():
        print("I am Class A")


class B(A):
    @staticmethod
    def print_b():
        print("I am Class B")


class C(B):
    @staticmethod
    def print_c():
        print("I am Class C")


B.print_a()
C.print_a()
C.print_b()
C.print_c()"""

"""Multiple Inheritance
class A:
    @staticmethod
    def print_a():
        print("I am Class A")


class B:
    @staticmethod
    def print_b():
        print("I am Class B")


class C(A, B):
    @staticmethod
    def print_c():
        print("I am Class C")


C.print_a()
C.print_b()
C.print_c()"""
