class Employee:
    def __init__(self, id, n, s):  # Parameterized Constructor
        self.eid = id
        self.ename = n
        self.salary = s

    def display(self):  # method
        print("Eid:", self.eid)
        print("Ename:", self.ename)
        print("Salary:", self.salary)

print("Enter ID, Name, and Salary:")
id = int(input())
name = input()
sal = float(input())
e2 = Employee(id, name, sal)  # object
e2.display()