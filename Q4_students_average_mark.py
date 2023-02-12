total_marks = 0
total_students = 0
best_mark = 0
best_student = ""

while True:
    name = input("Enter your name, (X to Exit):").title()

    if name == "X":
        break
    else:
        mark = int(input("Enter your mark:"))

    total_marks = total_marks + mark
    total_students = total_students + 1

    if mark >= best_mark:
        best_mark = mark
        best_student = name

average_mark = total_marks / total_students
print(f"The classes average mark was {average_mark}")
print(f"The top student was {best_student} with a mark of {best_mark}")
