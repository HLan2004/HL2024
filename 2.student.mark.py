class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.mark = {}

    def input_students():
        num_students = int(input("Enter number of students: "))
        students = []
        for _ in range(num_students):
            id = input("Enter Student id: ")
            name = input("Enter Student name: ")
            DoB = input("Enter Student Date of Birth: ")
            student = Student(id, name, DoB)
            students += [student]
        return students
    
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
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
                student.mark[course.id] = input(f"Enter marks for {student.name} in {course.name}: ")

    def studentslists(students):
        print("\nList of students:")
        for student in students:
            print(f"Student ID: {student.id} || Student Name: {student.name} || Date of Birth: {student.DoB}\n")

    def courseslists(courses):
        print("\nList of courses:")
        for course in courses:
            print(f"Course ID: {course.id} || Course Name: {course.name}\n")

    def print_marks(students, courseid):
        for student in students:
            print(f"Marks for {student.name} in Course {courseid}: {student.mark.get(courseid)}\n")

students = Student.input_students()
courses = Course.input_courses()
Course.input_marks(students, courses)
Course.studentslists(students)
Course.courseslists(courses)

courseid = input("\nPlease enter a Course id to show marks: ")
Course.print_marks(students, courseid)

while True:
    courseid = input("\nContinue to enter Course id or press 'n' to quit: ")
    if courseid.lower() == 'n':
        break
    Course.print_marks(students, courseid)