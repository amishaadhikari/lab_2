s = {}
while True:
    print('******** STUDENT MANAGEMENT SYSTEM ********')
    print("1. Add new student records")
    print("2. View report of all students")
    print("3. Display topper")
    print("4. Search for student by roll number")
    print("5. Display students who have failed")
    print("6. Update marks of any student")
    print("7. Exit")
    choice = int(input("Enter your choice (1-7): "))
    if choice == 1:
        roll = input("Enter roll number of student: ")
        if roll in s:
            print("Student with this roll number already exists.")
        else:
            name = input("Enter name: ")
            sub = ['Electronics', 'Electric Circuit', 'Maths', 'Advanced Programming', 'Chemistry']
            marks = {}
            for subject in sub:
                score = int(input(f"Enter marks for {subject}: "))
                marks[subject] = score
            s[roll] = {"Name": name, "marks": marks}
            print("Student record added successfully.")
    elif choice == 2:
        if not s:
            print("No records found.")
        else:
            print("\nStudent Reports:")
            for roll, data in s.items():
                print(f'\nRoll No: {roll}')
                print(f'Name   : {data["Name"]}')
                for subject, score in data['marks'].items():
                    print(f'  {subject}: {score}')
                avg = sum(data['marks'].values()) / len(data['marks'])
                print(f'  Average: {avg:.2f}')
    elif choice == 3:
        if not s:
            print("No records found.")
        else:
            max_avg = -1
            toppers = []
            for roll, data in s.items():
                total = sum(data['marks'].values())
                avg = total / len(data['marks'])
                if avg > max_avg:
                    max_avg = avg
                    toppers = [(roll, data['Name'], avg)]
                elif avg == max_avg:
                    toppers.append((roll, data['Name'], avg))
            print("\nTopper(s) of the Class:")
            for t in toppers:
                print(f"Roll: {t[0]}, Name: {t[1]}, Average Marks: {t[2]:.2f}")
    elif choice == 4:
        roll = input("Enter roll number to search: ")
        if roll in s:
            data = s[roll]
            print(f"\nRoll No: {roll}")
            print(f"Name   : {data['Name']}")
            for subject, score in data['marks'].items():
                print(f"  {subject}: {score}")
            avg = sum(data['marks'].values()) / len(data['marks'])
            print(f"  Average: {avg:.2f}")
        else:
            print("Student not found.")
    elif choice == 5:
        print("\nStudents who failed in one or more subjects (marks < 40):")
        found = False
        for roll, data in s.items():
            failed_subjects = [sub for sub, score in data['marks'].items() if score < 40]
            if failed_subjects:
                found = True
                print(f"{data['Name']} (Roll: {roll}) failed in: {', '.join(failed_subjects)}")
        if not found:
            print("No student has failed in any subject.")
    elif choice == 6:
        roll = input("Enter roll number to update marks: ")
        if roll in s:
            subject = input("Enter subject to update: ")
            if subject in s[roll]['marks']:
                new_mark = int(input("Enter new mark: "))
                s[roll]['marks'][subject] = new_mark
                print("Marks updated successfully.")
            else:
                print("Subject not found.")
        else:
            print("Student not found!!")
    elif choice == 7:
        print("Exiting program!!!")
        break
    else:
        print("Invalid choice!!!")