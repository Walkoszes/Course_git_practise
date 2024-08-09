from functions import *

# Main function to provide user interface
def main():
    create_tables()

    while True:
        print("1.Add new student")
        print("2.Add new course")
        print("3.View all students")
        print("4.View all courses")
        print("5.Register student for course")
        print("6.View students in a course")
        print("7.Exit")
        choice = input("Enter choice:")

        if choice == '1':
            name = input("Enter student name:")
            age = int(input("Enter student age:"))
            major = input("Enter student major:")
            add_student(name, age, major)
        elif choice == '2':
            course_name = input("Enter course name:")
            instructor = input("Enter instructor's name:")
            add_course(course_name, instructor)
        elif choice == '3':
            view_students()
        elif choice == '4':
            view_courses()
        elif choice == '5':
            student_id = int(input("Enter student's id:"))
            course_id = int(input("Enter course's id:"))
            register_student_for_course(student_id, course_id)
        elif choice == '6':
            course_id = int(input("Enter course's id:"))
            view_students_in_course(course_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice.")
main()