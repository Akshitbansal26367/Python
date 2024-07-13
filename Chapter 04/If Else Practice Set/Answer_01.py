# Calculate student grade
marks = int(input("Enter the marks : "))
if marks > 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 45:
    print("Grade D")
elif marks >= 25:
    print("Grade E")
else:
    print("Grade F")
