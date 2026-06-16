class Employee:
    def __init__(self):  # Constructor
        self.eid = -1
        self.ename = ""
        self.salary = -1.0

    def getData(self):  # method
        print("Enter ID, Name, and Salary:")
        self.eid = int(input())
        self.ename = input()
        self.salary = float(input())

    def display(self):  # method
        print("Eid:", self.eid)
        print("Ename:", self.ename)
        print("Salary:", self.salary)


e = Employee()  # object

e.getData()
e.display()

