from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

from database import initialize_database, get_connection
from student_service import add_student, view_all_students, search_student_by_id
from student_service import update_student, delete_student
from models import Student

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret"


@app.route("/")
def index():
    search_query = request.args.get("search", "").strip()
    edit_id = request.args.get("edit", type=int)

    students = view_all_students()

    if search_query:
        connection = get_connection()

        try:
            students = connection.execute(
                """
                SELECT * FROM students
                WHERE name LIKE ? COLLATE NOCASE
                   OR roll_number LIKE ? COLLATE NOCASE
                   OR email LIKE ? COLLATE NOCASE
                ORDER BY id
                """,
                (
                    f"%{search_query}%",
                    f"%{search_query}%",
                    f"%{search_query}%"
                )
            ).fetchall()
        except sqlite3.Error:
            flash("Unable to search student records.", "error")
            students = []
        finally:
            connection.close()

    editing_student = None

    if edit_id:
        editing_student = search_student_by_id(edit_id)

        if editing_student is None:
            flash("Student not found.", "error")

    connection = get_connection()

    try:
        stats = connection.execute(
            """
            SELECT COUNT(*) AS total,
                   AVG(gpa) AS average,
                   MAX(gpa) AS highest,
                   MIN(gpa) AS lowest
            FROM students
            """
        ).fetchone()

        total_students = stats["total"]
        average_gpa = stats["average"] or 0
        highest_gpa = stats["highest"] or 0
        lowest_gpa = stats["lowest"] or 0

        distribution = connection.execute(
            """
            SELECT
                CASE
                    WHEN gpa >= 9 THEN '9–10'
                    WHEN gpa >= 8 THEN '8–8.99'
                    WHEN gpa >= 7 THEN '7–7.99'
                    WHEN gpa >= 6 THEN '6–6.99'
                    ELSE 'Below 6'
                END AS gpa_range,
                COUNT(*) AS total
            FROM students
            GROUP BY gpa_range
            ORDER BY MIN(gpa)
            """
        ).fetchall()

        chart_labels = [row["gpa_range"] for row in distribution]
        chart_values = [row["total"] for row in distribution]

    except sqlite3.Error:
        total_students = 0
        average_gpa = 0
        highest_gpa = 0
        lowest_gpa = 0
        chart_labels = []
        chart_values = []
        flash("Unable to load dashboard statistics.", "error")

    finally:
        connection.close()

    return render_template(
        "index.html",
        students=students,
        search_query=search_query,
        editing_student=editing_student,
        total_students=total_students,
        average_gpa=average_gpa,
        highest_gpa=highest_gpa,
        lowest_gpa=lowest_gpa,
        chart_labels=chart_labels,
        chart_values=chart_values
    )


@app.route("/add", methods=["POST"])
def add():
    student = Student(
        roll_number=request.form.get("roll_number", "").strip(),
        name=request.form.get("name", "").strip(),
        email=request.form.get("email", "").strip(),
        gpa=request.form.get("gpa", "").strip()
    )

    success, message = add_student(student)

    flash(message, "success" if success else "error")

    return redirect(url_for("index"))


@app.route("/update/<int:student_id>", methods=["POST"])
def update(student_id):
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    gpa = request.form.get("gpa", "").strip()

    success, message = update_student(
        student_id, name, email, gpa
    )

    flash(message, "success" if success else "error")

    return redirect(url_for("index"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    success, message = delete_student(student_id)

    flash(message, "success" if success else "error")

    return redirect(url_for("index"))


@app.route("/api/students")
def api_students():
    students = view_all_students()

    return {
        "students": [
            {
                "id": student["id"],
                "roll_number": student["roll_number"],
                "name": student["name"],
                "email": student["email"],
                "gpa": student["gpa"]
            }
            for student in students
        ]
    }


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)