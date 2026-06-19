class Employee:
    def __init__(self):
        print("This is the Constructor of an Employee")
    a=1
class  Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("This is the Constructor of an Programmer")
    b=2
class Manage(Programmer):
    c=3
    def __init__(self):
        super().__init__()
        print("This is the Constructor of an Manager")

o=Employee()
print(o.a)

o=Programmer()
print(o.a,o.b)

o=Manage()
print(o.a,o.b,o.c)
