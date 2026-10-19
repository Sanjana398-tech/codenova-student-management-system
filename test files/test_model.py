from models import Student


student = Student(
    roll_number="101",
    name="Sanjana Naik",
    email="sanjana@example.com",
    gpa=9.1
)

print("Student Details")
print("------------------------")
print("Roll Number:", student.roll_number)
print("Name:", student.name)
print("Email:", student.email)
print("GPA:", student.gpa)