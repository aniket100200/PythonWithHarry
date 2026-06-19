class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        value=value.split(" ")
        self.fname=value[0]
        self.lname=value[1]
e=Employee()
e.a=45
e.name="Aniket Khangar"
print(e.name)