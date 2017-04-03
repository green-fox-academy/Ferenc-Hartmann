#Create Student and Teacher classes
#Student
#   learn()
#   question(teacher) -> calls the teachers answer method
#Teacher
#   teach(student) -> calls the students learn method
#   answer()

class Student:
    def learn(self):
        print("learn")
    def question(self):
        Teacher.answer()

class Teacher:
    def teach(self):
        Student.learn()
    def answer(self):
        print("answer")

bubo = Teacher()
pali = Student()
bubo.teach()
pali.question()
