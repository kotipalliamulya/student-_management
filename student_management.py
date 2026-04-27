class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        try:
            marks = float(input("Enter marks: "))
        except ValueError:
            print("Invalid marks! Try again.")
            return

        self.students.append(Student(name, marks))
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n--- Student List ---")
        for s in self.students:
            print(s)

    def calculate_average(self):
        if not self.students:
            print("No data available.")
            return

        avg = sum(s.marks for s in self.students) / len(self.students)
        print(f"Average Marks: {avg:.2f}")

    def show_topper(self):
        if not self.students:
            print("No data available.")
            return

        topper = max(self.students, key=lambda s: s.marks)
        print(f"Topper: {topper.name} ({topper.marks})")

    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Average Marks")
            print("4. Show Topper")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.calculate_average()
            elif choice == "4":
                self.show_topper()
            elif choice == "5":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Try again.")


if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()