class Student:

    def __init__(self):   # constructor
        print("constructor execution")
        self.name = "akshay"                  #instance veriable
        self.rollno = 1314
        self.dept = "mechanical"
        print(self.dept)
    def display(self): #method
        print(f"my name is {self.name},my roll no is {self.rollno},i am from {self.dept} department")


s = Student()  #object
s2 = Student()
print(s.dept)
print(s.rollno)
print(s.name)
s.display()
print(s2.rollno)
print(id(s))
print(id(s2))
s2.display()
Student()