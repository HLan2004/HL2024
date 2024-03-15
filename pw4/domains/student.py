class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.marks = {}

    def input_mark(self, course, mark):
        self.marks[course.id] = round(mark)