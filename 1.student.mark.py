class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for num_students in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append(Student(id, name, dob))
    return students

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for num_courses in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append(Course(id, name))
    return courses

def input_marks(students, courses):
    for course in courses:
        for student in students:
            student.marks[course.id] = input(f"Enter marks for {student.name} in {course.name}: ")

def list_courses(courses):
    for course in courses:
        print(f"Course ID: {course.id}, Course Name: {course.name}")

def list_students(students):
    for student in students:
        print(f"Student ID: {student.id}, Student Name: {student.name}, DoB: {student.dob}")

def show_marks(students, course_id):
    for student in students:
        print(f"Marks for {student.name} in course {course_id}: {student.marks.get(course_id, 'N/A')}")

    
students = input_students()
courses = input_courses()
input_marks(students, courses)
    
print("\nList of students:")
list_students(students)
    
print("\nList of courses:")
list_courses(courses)

course_id = input("\nEnter a course id to show marks: ")
show_marks(students, course_id)