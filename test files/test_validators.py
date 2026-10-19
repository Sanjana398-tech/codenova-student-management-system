from validators import (
    validate_name,
    validate_roll_number,
    validate_email,
    validate_gpa
)


print("NAME VALIDATION")
print(validate_name("Sanjana"))
print(validate_name(""))

print("\nROLL NUMBER VALIDATION")
print(validate_roll_number("101"))
print(validate_roll_number(""))

print("\nEMAIL VALIDATION")
print(validate_email("sanjana@example.com"))
print(validate_email("invalid-email"))

print("\nGPA VALIDATION")
print(validate_gpa("9.1"))
print(validate_gpa("15"))
print(validate_gpa("hello"))