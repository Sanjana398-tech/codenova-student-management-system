from dataclasses import dataclass


@dataclass
class Student:
    roll_number: str
    name: str
    email: str
    gpa: float
    id: int = 0