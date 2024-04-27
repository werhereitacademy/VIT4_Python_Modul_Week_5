class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        if average >= 90:
            return 'O'
        elif average >= 80:
            return 'E'
        elif average >= 70:
            return 'A'
        elif average >= 55:
            return 'P'
        elif average >= 40:
            return 'D'
        else:
            return 'T'

# Input section
firstName, lastName, idNum = input("Enter student's first name, last name, and ID number separated by space: ").split()
numScores = int(input("Enter the number of scores: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))

# Create Student object
s = Student(firstName, lastName, idNum, scores)

# Output section
print("\nStudent Information:")
s.printPerson()
print("Grade:", s.calculate())
