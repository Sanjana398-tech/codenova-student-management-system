import sqlite3

from database import get_connection
from models import Student
from validators import (
    validate_name,
    validate_roll_number,
    validate_email,
    validate_gpa
)


def add_student(student):
    """Validate and add a student to the database."""

    # Validate name
    valid, message = validate_name(student.name)

    if not valid:
        return False, message

    # Validate roll number
    valid, message = validate_roll_number(student.roll_number)

    if not valid:
        return False, message

    # Validate email
    valid, message = validate_email(student.email)

    if not valid:
        return False, message

    # Validate GPA
    valid, message = validate_gpa(student.gpa)

    if not valid:
        return False, message

    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT INTO students (roll_number, name, email, gpa)
            VALUES (?, ?, ?, ?)
            """,
            (
                student.roll_number.strip(),
                student.name.strip(),
                student.email.strip(),
                float(student.gpa)
            )
        )

        connection.commit()

        return True, "Student added successfully!"

    except sqlite3.IntegrityError:
        return False, (
            "Roll number or email already exists, "
            "or the student data violates a database constraint."
        )

    except sqlite3.Error as error:
        return False, f"Database error: {error}"

    finally:
        connection.close()

def view_all_students():
    """Retrieve all student records from the database."""

    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM students ORDER BY id"
        )

        students = cursor.fetchall()

        return students

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []

    finally:
        connection.close()

def search_student_by_id(student_id):
    """Find a student using their database ID."""

    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        return cursor.fetchone()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return None

    finally:
        connection.close()

def search_student_by_name(name):
    """Search students by a partial, case-insensitive name."""

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT * FROM students
            WHERE name LIKE ? COLLATE NOCASE
            ORDER BY name
            """,
            (f"%{name.strip()}%",)
        )

        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []

    finally:
        connection.close()

def update_student(student_id, name, email, gpa):
    """Update an existing student's details."""

    valid, message = validate_name(name)
    if not valid:
        return False, message

    valid, message = validate_email(email)
    if not valid:
        return False, message

    valid, message = validate_gpa(gpa)
    if not valid:
        return False, message

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE students
            SET name = ?, email = ?, gpa = ?
            WHERE id = ?
            """,
            (name.strip(), email.strip(), float(gpa), student_id)
        )

        if cursor.rowcount == 0:
            return False, "Student not found."

        connection.commit()
        return True, "Student updated successfully!"

    except sqlite3.IntegrityError:
        return False, "Email already exists."

    except sqlite3.Error as error:
        return False, f"Database error: {error}"

    finally:
        connection.close()

def delete_student(student_id):
    """Delete a student using their database ID."""

    connection = get_connection()

    try:
        cursor = connection.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        if cursor.rowcount == 0:
            return False, "Student not found."

        connection.commit()
        return True, "Student deleted successfully!"

    except sqlite3.Error as error:
        return False, f"Database error: {error}"

    finally:
        connection.close()