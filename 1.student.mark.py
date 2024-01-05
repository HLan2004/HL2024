def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for num_students in range(num_students):
        id = input("Enter Student id: ")
        name = input("Enter Student name: ")
        DoB = input("Enter Student Date of Birth: ")
        student = {'id': id, 'name': name, 'DoB':DoB, 'mark': {}}
        students += [student]
    return students

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for num_courses in range(num_courses):
        id = input("Enter Course id: ")
        name = input("Enter Course name: ")
        course = {'id':id, 'name': name}
        courses += [course]
    return courses 

def input_marks(students, courses):
    for course in courses:
        for student in students:
            student['mark'][course['id']] = input(f"Enter marks for {student['name']} in {course['name']}: ")

def studentslists(students):
    print("\nList of students:")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}, Date of Birth: {student['DoB']}")

def courseslists(courses):
    print("\nList of courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

def print_marks(students, courseid):
    for student in students:
        print(f"Marks for {student['name']} in Course {courseid}: {student['mark'].get(courseid)}")


students = input_students()
courses = input_courses()

input_marks(students, courses)
    
studentslists(students)
    
courseslists(courses)

courseid = input("\nPlease enter a Course id to show marks: ")
print_marks(students, courseid)

while True:
    courseid = input("\nContinue to enter Course id or press 'n' to quit: ")
    if courseid.lower() == 'n':
        break
    print_marks(students, courseid)