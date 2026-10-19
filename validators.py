import re


def validate_name(name):
    """Check whether the student name is valid."""

    if not name or not name.strip():
        return False, "Name cannot be empty."

    if not name.strip().replace(" ", "").isalpha():
        return False, "Name must contain only letters and spaces."

    return True, ""


def validate_roll_number(roll_number):
    """Check whether the roll number is valid."""

    if not roll_number or not roll_number.strip():
        return False, "Roll number cannot be empty."

    return True, ""


def validate_email(email):
    """Check whether the email address has a valid format."""

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not email or not email.strip():
        return False, "Email cannot be empty."

    if not re.fullmatch(pattern, email.strip()):
        return False, "Please enter a valid email address."

    return True, ""


def validate_gpa(gpa):
    """Check whether GPA is a valid number between 0 and 10."""

    try:
        value = float(gpa)

        if not 0 <= value <= 10:
            return False, "GPA must be between 0 and 10."

        return True, ""

    except (ValueError, TypeError):
        return False, "GPA must be a valid number."