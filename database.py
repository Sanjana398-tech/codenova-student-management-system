import sqlite3
from pathlib import Path


# Get the project directory
BASE_DIR = Path(__file__).resolve().parent

# Define the database location
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "students.db"


def get_connection():
    """Connect to the SQLite database."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """Create the students table if it does not exist."""

    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                roll_number TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                gpa REAL NOT NULL CHECK (gpa >= 0 AND gpa <= 10)
            )
        """)

        connection.commit()
        print("Database initialized successfully!")

    except sqlite3.Error as error:
        print(f"Database initialization failed: {error}")

    finally:
        connection.close()