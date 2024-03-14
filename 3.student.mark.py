import math
import numpy as np

class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.mark = {}
        self.credits = {}
        self.gpa = 0

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
    
    def studentslists(students):
        print("\nList of students:")
        for student in students:
            print(f"Student ID: {student.id} || Student Name: {student.name} || Date of Birth: {student.DoB}\n")


    def calculate_gpa(self):
        weighted_marks = np.array(list(self.mark.values()))
        credits = np.array(list(self.credits.values()))
        self.gpa = np.sum(weighted_marks * credits) / np.sum(credits)
    
    def calculate_gpas(students):
        for student in students:
            student.calculate_gpa()

    def sort_students_by_gpa(students):
        students.sort(key=lambda student: student.gpa, reverse=True)
    

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def input_marks(self, students):
        for student in students:
            mark = float(input(f"Enter marks for {student.name} in {self.name}: "))
            student.mark[self.id] = math.floor(mark * 10) 
            student.credits[self.id] = self.credit

    def input_courses():
        num_courses = int(input("Enter number of courses: "))
        courses = []
        for _ in range(num_courses):
            id = input("Enter Course id: ")
            name = input("Enter Course name: ")
            credit = int(input("Enter Course credit: "))
            course = Course(id, name, credit)
            courses.append(course)
        return courses
    
    def courseslists(courses):
        print("\nList of courses:")
        for course in courses:
            print(f"Course ID: {course.id} || Course Name: {course.name}\n")


students = Student.input_students()
courses = Course.input_courses()

for course in courses:
    course.input_marks(students)

Student.studentslists(students)
Course.courseslists(courses)


Student.calculate_gpas(students)
Student.sort_students_by_gpa(students)

for student in students:
    print(f"Student ID: {student.id} +++ GPA: {student.gpa}\n")