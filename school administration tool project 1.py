class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_student_names(self):
        return [student.name for student in self.students]

    def get_average_grade(self):
        total_grade = sum([student.grade for student in self.students])
        return total_grade / len(self.students)

school = School()

while True:
    print("\nWelcome to School Administration Tool")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student Names")
    print("4. View Average Grade")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade: "))
        student = Student(name, age, grade)
        school.add_student(student)
        print("Student added successfully.")

    elif choice == '2':
        name = input("Enter student name: ")
        for student in school.students:
            if student.name == name:
                school.remove_student(student)
                print("Student removed successfully.")
                break
        else:
            print("Student not found.")

    elif choice == '3':
        print("Student names:")
        for name in school.get_student_names():
            print("- " + name)

    elif choice == '4':
        print("Average grade: %.2f" % school.get_average_grade())

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
