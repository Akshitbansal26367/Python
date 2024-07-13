# Determine if student is allowed to sit in examination
class_held = int(input("Enter number of classes held : "))
class_attend = int(input("Enter class attended : "))

percentage = class_attend / class_held * 100
if percentage >= 75:
    print("Child allowed to  sit in exam")
else:
    print("Child not allowed to sit in exam")
