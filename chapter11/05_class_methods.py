class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

a=Employee()
a.a=45
a.show()