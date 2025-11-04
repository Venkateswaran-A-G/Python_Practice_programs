#Create a class Student with attributes name & marks, and method to print details
#Inherit Student class to create GraduateStudent with additional attribute degree.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def printAll(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
class GraduateStudent(Student):
    def __init__(self,name,marks,degree):
        super().__init__(name,marks)
        self.degree=degree
    def display(self):
        super().printAll()
        print("Degree: ",self.degree)