from database import initialize_database
from student_service import (
    add_student,
    view_all_students,
    search_student_by_id,
    search_student_by_name,
    update_student,
    delete_student
)
from models import Student


def display_menu():
    print("\n" + "=" * 45)
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Search Student by Name")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")
    print("=" * 45)


def add_student_menu():
    print("\n--- Add Student ---")

    roll_number = input("Enter roll number: ")
    name = input("Enter student name: ")
    email = input("Enter email: ")
    gpa = input("Enter GPA (0-10): ")

    student = Student(
        roll_number=roll_number,
        name=name,
        email=email,
        gpa=gpa
    )

    success, message = add_student(student)
    print(message)


def view_students_menu():
    print("\n--- All Students ---")
    students = view_all_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 35)
        print(f"ID: {student['id']}")
        print(f"Roll Number: {student['roll_number']}")
        print(f"Name: {student['name']}")
        print(f"Email: {student['email']}")
        print(f"GPA: {student['gpa']}")


def search_by_id_menu():
    print("\n--- Search Student by ID ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = search_student_by_id(student_id)

    if student:
        print(f"ID: {student['id']}")
        print(f"Roll Number: {student['roll_number']}")
        print(f"Name: {student['name']}")
        print(f"Email: {student['email']}")
        print(f"GPA: {student['gpa']}")
    else:
        print("Student not found.")


def search_by_name_menu():
    print("\n--- Search Student by Name ---")
    name = input("Enter full or partial name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    students = search_student_by_name(name)

    if not students:
        print("No matching students found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Roll Number: {student['roll_number']} | "
            f"Name: {student['name']} | "
            f"Email: {student['email']} | "
            f"GPA: {student['gpa']}"
        )


def update_student_menu():
    print("\n--- Update Student ---")

    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = search_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print("Leave a field blank to keep its current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    email = input(f"Email [{student['email']}]: ").strip()
    gpa = input(f"GPA [{student['gpa']}]: ").strip()

    name = name or student["name"]
    email = email or student["email"]
    gpa = gpa or str(student["gpa"])

    success, message = update_student(
        student_id, name, email, gpa
    )
    print(message)


def delete_student_menu():
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = search_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print(f"Student: {student['name']}")
    confirmation = input("Are you sure you want to delete? (yes/no): ")

    if confirmation.strip().lower() == "yes":
        success, message = delete_student(student_id)
        print(message)
    else:
        print("Deletion cancelled.")


def main():
    initialize_database()

    while True:
        display_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_student_menu()
        elif choice == "2":
            view_students_menu()
        elif choice == "3":
            search_by_id_menu()
        elif choice == "4":
            search_by_name_menu()
        elif choice == "5":
            update_student_menu()
        elif choice == "6":
            delete_student_menu()
        elif choice == "7":
            print("Thank you for using the Student Record Management System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()