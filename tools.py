import sqlite3
from langchain.tools import tool


@tool
def get_student_info(student_id: str) -> str:
    """Get the name and department of a student using their student ID."""

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name, department
        FROM students
        WHERE student_id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    if student is None:
        return f"No student found with ID {student_id}"

    name, department = student

    return f"Name: {name}, Department: {department}"

@tool
def get_student_marks(student_id: str) -> str:
    """Get the Python, Database, AI, and Web marks of a student using their student ID."""

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT python, database, ai, web
        FROM students
        WHERE student_id = ?
        """,
        (student_id,)
    )

    marks = cursor.fetchone()

    connection.close()

    if marks is None:
        return f"No student found with ID {student_id}"

    python_mark, database_mark, ai_mark, web_mark = marks

    return (
        f"Python: {python_mark}, "
        f"Database: {database_mark}, "
        f"AI: {ai_mark}, "
        f"Web: {web_mark}"
    )

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression such as a total or average."""
    
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error calculating expression: {e}"
    
@tool
def get_passing_rules() -> str:
    """Get the university rules required for a student to pass."""
    
    return (
        "University passing rules: "
        "Minimum overall average: 40%. "
        "Minimum mark in each subject: 35%."
    )
    