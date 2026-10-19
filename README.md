# Student Record Management System

A Python-based Student Record Management System developed as part of the CodeNova Python Programming Internship.

## Features

- Add new student records
- View all student records
- Search students by ID
- Search students by full or partial name
- Update existing student records
- Delete student records with confirmation
- Validate student names, email addresses, and GPA
- Prevent duplicate roll numbers and email addresses
- Store records persistently using SQLite
- Handle invalid inputs gracefully
- View GPA distribution and class statistics on the web dashboard
- Switch between light and dark dashboard themes

## Technologies Used

- Python
- SQLite
- Flask
- VS Code
- Git and GitHub

## Project Structure

Student_Record_Management_System/
- main.py
- database.py
- models.py
- validators.py
- student_service.py
- data/
- screenshots/

## Requirements

- Python 3.10 or later
- Install the web application dependency with `python -m pip install -r requirements.txt`.

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Install dependencies:

   python -m pip install -r requirements.txt

5. To use the web dashboard, run:

   python web_app.py

6. Open `http://127.0.0.1:5000` in your browser.

To use the interactive command-line menu instead, run:

   python main.py

Then select an option from the menu.

## Database

The application uses SQLite to store student records. Records remain available after the application is restarted.

## Validation

The application validates student names, email addresses, and GPA values. Roll numbers and email addresses must be unique.

## Learning Outcomes

- Python functions and modules
- Object-oriented programming concepts
- SQLite database operations
- CRUD operations
- Input validation
- Exception handling
- Modular project organization

## Internship

Developed as a project for the CodeNova Python Programming Internship.