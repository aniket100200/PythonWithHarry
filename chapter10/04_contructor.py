class Employee:
    language="Pythong"
    salary=12345

    def __init__(self,name,salary,language): # dunder method
        self.name=name
        self.salary=salary
        self.language=language
        print("I'm Creating an object")

    def getInfo(this):
        print(f"The langugae is {this.language} and Salary is {this.salary} ")
    
    @staticmethod
    def greet():
        print(f"Hello Brother")

aniket=Employee("Harry",1300000,"javascript")
print(aniket.salary)