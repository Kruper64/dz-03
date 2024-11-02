class StudySubject:
    name: str
    hours: int
    enable: bool
    index: int

    def __init__(self, name: str, hours: int, enable: bool, index: int):
        self.name = name
        self.hours = hours
        self.enable = enable
        self.index = index

    def info_study(self):
        print(f'Study №{self.index}: {self.name} | {self.hours}')

mStudy = []
for x in range(1, 4):
    name = input("Введіть назву предмета №"+str(x)+":")
    hours = int(input("Введіть кількість годин по предмету №"+str(x)+":"))
    python = StudySubject(name, hours, enable=True, index=x)
    mStudy.append(python)

# python.info_study()

class Student:
    nameStudent: str
    surnameStudent: str
    study: list

    def __init__(self, nameStudent: str, surnameStudent: str, study: list):
        self.nameStudent = nameStudent
        self.surnameStudent = surnameStudent
        self.study = study

    def info_student(self):
        print("----------------------Повна інформація по студенту:")
        print(f'Student: {self.nameStudent} | {self.surnameStudent}')

    def info_all(self):
        self.info_student()
        for x in range(0, 3):
            self.study[x].info_study()
class Group:
    nameGroup: str
    Quantity: int
    age: str
    Students: list

    def __init__(self, nameGroup: str, Quantity: int, age: str, Students: list ):
        self.nameGroup = nameGroup
        self.Quantity = Quantity
        self.age = age
        self.Students = Students

    def info_all(self):
        print("----------------------Повна інформація по групі:")
        print(f'Group: {self.nameGroup} | {self.Quantity} | {self.age}')
        for x in range(0, len(mStudents)):
            self.Students[x].info_all()

mStudents = []
for x in range(1, 4):
    nameSt = input("Введіть ім'я студента №"+str(x)+":")
    surname = input("Введіть призвище студента №"+str(x)+":")
    student = Student(nameStudent=nameSt, surnameStudent=surname, study=mStudy)
    mStudents.append(student)
    # student.info_all()
nameGroup = input("Введіть назву групи:")
age = input("Введіть вікову категорію:")
Quantity = len(mStudents)
group = Group(nameGroup=nameGroup, Quantity=Quantity, age=age, Students=mStudents)
group.info_all()