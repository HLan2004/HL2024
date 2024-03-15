import output as output
import input as input
from domains.student import Student
from domains.course import Course

students = input.input_students()
courses = input.input_courses()

input.input_marks(students, courses)

print("\nList of students:")
output.list_student(students)

print("\nList of courses:")
output.list_course(courses)

print('\nList of Students mark: ')
output.list_mark(students, courses)