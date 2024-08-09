import sqlite3

# Function to create tables
def create_tables():
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()
        with open('schemas.sql', 'r') as schema_file:
            schema = schema_file.read()
            cursor.executescript(schema)
        cucu.commit()

# Function to add a new student
def add_student(name, age, major):
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
        cucu.commit()

# Function to add a new course
def add_course(course_name, instructor):
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (course_name, instructor))
        cucu.commit()

# Function to view all students
def view_students():
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(student)

# Function to view all courses
def view_courses():
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        for course in courses:
            print(course)

# Function to register a student for a course
def register_student_for_course(student_id, course_id):
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        cucu.commit()

# Function to view students registered for a specific course
def view_students_in_course(course_id):
    with sqlite3.connect("university.db") as cucu:
        cursor = cucu.cursor()

        # Fetch student_ids for the given course_id
        cursor.execute("SELECT student_id FROM student_courses WHERE course_id = ?", (course_id,))
        student_ids = cursor.fetchall()

        if not student_ids:
            print("No students registered for this course.")
            return

        # Iterate over the fetched student_ids
        for student_id in student_ids:
            cursor.execute("SELECT name, age, major FROM students WHERE id = ?", (student_id[0],))
            student = cursor.fetchone()
            print(student)