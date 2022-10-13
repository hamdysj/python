class Student:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def set_name(self, n):
        self.name = n

    def get_name(self):
        print('Student name is ', self.name)

    def set_mark(self, mrk):
        self.mark = mrk

    def get_mark(self):
        print('Student score is ', self.mark)

    def stud_info(self):
        print("Student Name: ", self.name, " Student Score: ", self.mark)


stud1 = Student("Jamal", 56)
stud2 = Student("Bashir", 78)

stud1.stud_info()

stud1.set_name("Quadri")
stud1.stud_info()
