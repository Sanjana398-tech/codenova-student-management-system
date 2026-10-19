from student_service import (
    update_student,
    delete_student,
    search_student_by_id
)


# Update student ID 1
success, message = update_student(
    student_id=1,
    name="Sanjana Naik",
    email="sanjana@example.com",
    gpa=9.5
)

print(message)


# Verify the update
student = search_student_by_id(1)

if student:
    print("\nUpdated Student Details")
    print("Name:", student["name"])
    print("Email:", student["email"])
    print("GPA:", student["gpa"])


# Delete student ID 1
# Uncomment the following lines ONLY when you want to test deletion.

# success, message = delete_student(1)
# print(message)