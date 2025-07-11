def input_students():
    n = int(input("Enter number of students: "))
    students = {}
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = []
        for j in range(3):
            m = int(input("Enter marks: "))
            marks.append(m)
        students[name] = marks
    return students
def display_averages(students):
    averages = {}
    print("\nAverage Marks:")
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        averages[name] = avg
        print(f"{name}: {avg:.2f}")
    return averages
def find_topper(averages):
    topper = max(averages, key=averages.get)
    print(f"\nTopper: {topper} with average marks {averages[topper]:.2f}")
def update_marks(students):
    update_name = input("\nEnter the name of student to update marks: ")
    if update_name in students:
        new_marks = []
        for j in range(3):
            m = int(input("Enter new mark: "))
            new_marks.append(m)
        students[update_name] = new_marks
        print(f"Marks updated for {update_name}.")
    else:
        print("Student not found.")
students = input_students()
averages = display_averages(students)
find_topper(averages)
update_marks(students)
averages = display_averages(students)
find_topper(averages)