# Program to Take in marks of 5 subjects and Display the Grade
maths = int(input("Enter marks in M : "))
chemistry = int(input("Enter marks in C : "))
physics = int(input("Enter marks in P : "))
english = int(input("Enter marks in E : "))
hindi = int(input("Enter marks in H : "))

percentage = (maths + chemistry + physics + english + hindi) / 5
print("\nThe percentage is", percentage, "%")

if percentage >= 90:
    print("\nGrade A")
elif percentage >= 80:
    print("\nGrade B")
elif percentage >= 60:
    print("\nGrade C")
elif percentage >= 50:
    print("\nGrade D")
elif percentage >= 40:
    print("\nGrade E")
else:
    print("\nGrade F")
