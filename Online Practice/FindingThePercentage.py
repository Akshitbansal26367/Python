def student_avg(stu_marks, q_name):
    avg = 0
    for key, value in stu_marks.items():
        if key == q_name:
            avg = sum(value) / len(value)
    print("The average marks of student", q_name, "is", '{:.2f}'.format(avg))


n = int(input("Enter the total number of students : "))
print()
student_marks = {}
for _ in range(n):
    name, *line = input().split(" ")
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("\nEnter name whose average marks are to be calculated : ")
student_avg(student_marks, query_name)
