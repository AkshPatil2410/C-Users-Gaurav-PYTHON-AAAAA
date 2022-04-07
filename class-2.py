class Employee:

    def __init__(self,name,empid,dept,position):
        self.name = name
        self.empid = empid
        self.dept = dept
        self.position = position
    def display(self):
        print(f"my name is {self.name},my employee id is {self.empid}, i am from {self.dept},act as a {self.position}")


e = Employee("akshay",1314,"qa","sr engineer")
e.display()
print(e.name)

e1 = Employee("shweta",1245,"prod","jr Engineer")
e1.display()