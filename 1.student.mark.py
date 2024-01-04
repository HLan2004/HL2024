class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.marks = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for num_students in range(num_students):
        id = input("Enter Student id: ")
        name = input("Enter Student name: ")
        DoB = input("Enter Student Date of Birth: ")
        students.append(Student(id, name, DoB))
    return students

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for num_courses in range(num_courses):
        id = input("Enter Course id: ")
        name = input("Enter Course name: ")
        courses.append(Course(id, name))
    return courses

def input_marks(students, courses):
    for Course in courses:
        for Student in students:
            Student.marks[Course.id] = input(f"Enter marks for {Student.name} in {Course.name}: ")

def list_students(students):
    for Student in students:
        print(f"Student ID: {Student.id}, Student Name: {Student.name}, DoB: {Student.DoB}")

def list_courses(courses):
    for Course in courses:
        print(f"Course ID: {Course.id}, Course Name: {Course.name}")

def show_marks(students, course_id):
    for Student in students:
        print(f"Marks for {Student.name} in Course {course_id}: {Student.marks.get(course_id)}")


students = input_students()
courses = input_courses()
input_marks(students, courses)
    
print("\nList of students:")
list_students(students)
    
print("\nList of courses:")
list_courses(courses)

course_id = input("\nEnter a Course id to show marks: ")
show_marks(students, course_id)