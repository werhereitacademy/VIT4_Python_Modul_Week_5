# Question 2
class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}

    def add_student(self, student_name, grade):
        self.students.append((student_name, grade))

    def add_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject

    def show_students(self):
        print("Student List:")
        for student in self.students:
            print("- {} ({})".format(student[0], student[1]))

    def show_teachers(self):
        print("Teacher List:")
        for teacher, subject in self.teachers.items():
            print("- {} ({})".format(teacher, subject))