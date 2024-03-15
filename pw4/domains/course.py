class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def input_mark(self, course, mark):
        self.marks[course.id] = round(mark)