total_marks = 0
total_students = 0
best_mark = 0
best_student = ""
students_list = []
grade = ""

while True:
    name = input("Enter your name, (X to Exit):").title()

    if name == "X":
        break
    else:
        mark = int(input("Enter your mark:"))

    if mark >= 90:
        grade = "A+"
    elif mark >= 85:
        grade = "A"
    elif mark >= 80:
        grade = "A-"
    elif mark >= 75:
        grade = "B+"
    elif mark >= 70:
        grade = "B"
    elif mark >= 65:
        grade = "B-"
    elif mark >= 60:
        grade = "C+"
    elif mark >= 55:
        grade = "C"
    elif mark >= 50:
        grade = "C-"
    elif mark >= 40:
        grade = "D"
    elif mark >= 0:
        grade = "E"

    students_list.append([name, grade])

    total_marks = total_marks + mark
    total_students = total_students + 1

    if mark >= best_mark:
        best_mark = mark
        best_student = name


average_mark = total_marks / total_students
print(f"The classes average mark was {average_mark}")
print(f"The top student was {best_student} with a mark of {best_mark}")

for students in students_list:
    print(students)
