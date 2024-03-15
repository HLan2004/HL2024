from domains.student import Student
from domains.course import Course

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for _ in range(num_students):
        id = input("Enter Student id: ")
        name = input("Enter Student name: ")
        DoB = input("Enter Student Date of Birth: ")
        student = Student(id, name, DoB)
        students.append(student)
    return students

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for _ in range(num_courses):
        id = input("Enter Course id: ")
        name = input("Enter Course name: ")
        course = Course(id, name)
        courses += [course]
    return courses

def input_marks(students, courses):
    for course in courses:
        for student in students:
            mark = float(input(f"Enter marks for {student.name} in {course.name}: "))
            student.input_mark(course, mark)