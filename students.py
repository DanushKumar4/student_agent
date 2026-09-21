import sqlite3


def get_student_info(student_id: str):
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

    return student


def get_student_marks(student_id: str):
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

    return marks