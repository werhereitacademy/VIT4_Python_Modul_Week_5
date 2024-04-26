

class School:

    school_name = "Anadolu Lisesi"
    establishment_year = 2001 

    students = []
    teachers = {}

    def __init__(self):
        pass

    def add_new_student(self, student_name, student_class):
        self.students.append({"Name": student_name, "Class": student_class})


    def add_new_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject


    def display_students_list(self):
        print(self.students)

    
    def display_teachers_list(self):
        print(self.teachers)

    
my_school = School()

my_school.add_new_student("Mehmet Kaya", 11)
my_school.add_new_student("Ali Demir", 11)
my_school.add_new_student("Muftafa Kar", 11)

my_school.add_new_teacher("Mahmut Can", "Bioligy")
my_school.add_new_teacher("Huseyin Yilmaz", "Math")
my_school.add_new_teacher("Ibrahim Tosun", "Physics")
print("\n\n")
my_school.display_students_list()
print("\n\n")
my_school.display_teachers_list()
print("\n\n")

    