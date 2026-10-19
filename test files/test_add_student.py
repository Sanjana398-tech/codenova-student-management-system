from database import get_connection


connection = get_connection()

try:
    cursor = connection.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    for student in students:
        print("ID:", student["id"])
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Email:", student["email"])
        print("GPA:", student["gpa"])
        print("-" * 30)

finally:
    connection.close()