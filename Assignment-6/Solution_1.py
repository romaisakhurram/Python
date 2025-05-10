# 1. Using Self
#Assignment :
class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student_1 = Student("Romaisa" , 90)
student_1.display()
