def list_student(students):
    for student in students:
        print(f"Student ID: {student.id} || Student Name: {student.name} || Date of Birth: {student.DoB}\n")

def list_course(courses):
    for course in courses:
        print(f"Course ID: {course.id} || Course Name: {course.name}\n")

def list_mark(students, courses):
    for student in students:
            for course in courses:
                print(f"Student ID: {student.id} || Marks for {student.name} in Course {course.name}: {student.marks.get(course.id)}\n")