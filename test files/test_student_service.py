from database import initialize_database
from student_service import (
    view_all_students,
    search_student_by_id,
    search_student_by_name
)


initialize_database()

# Test 1: View all students
print("\n========== ALL STUDENTS ==========")

students = view_all_students()

if students:
    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Roll No: {student['roll_number']} | "
            f"Name: {student['name']} | "
            f"Email: {student['email']} | "
            f"GPA: {student['gpa']}"
        )
else:
    print("No student records found.")


# Test 2: Search by database ID
print("\n========== SEARCH BY ID ==========")

student = search_student_by_id(1)

if student:
    print("Student found:", student["name"])
else:
    print("Student not found.")


# Test 3: Search by partial name
print("\n========== SEARCH BY NAME ==========")

students = search_student_by_name("sanj")

if students:
    for student in students:
        print(
            f"{student['name']} - "
            f"{student['email']} - "
            f"GPA: {student['gpa']}"
        )
else:
    print("No matching students found.")