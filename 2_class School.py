class School:
    def __init__(self, name, establishment_year):
        self.name = name
        self.establishment_year = establishment_year
        self.students = []
        self.teachers = {}

    def add_student(self, student_name, grade):
        self.students.append({"name": student_name, "grade": grade})

    def add_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject

    def display_student_list(self):
        print("Registered students:")
        for student in self.students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")

    def display_teacher_list(self):
        print("Teachers:")
        for teacher, subject in self.teachers.items():
            print(f"Name: {teacher}, Subject: {subject}")

# Sample usage
school = School("Ede School", 1990)
school.add_student("Ali Er", "10A")
school.add_student("Miriam Son", "11B")
school.add_teacher("Jan Kai", "Mathematics")
school.add_teacher("Regien Woort", "Physics")

school.display_student_list()
print("\n")
school.display_teacher_list()
