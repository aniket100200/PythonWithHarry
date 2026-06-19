class Employee:
    language="Pythong"
    salary=12345

    def getInfo(this):
        print(f"The langugae is {this.language} and Salary is {this.salary} ")
    
    @staticmethod
    def greet():
        print(f"Hello Brother")

harry=Employee()
# Employee.getInfo(harry)
harry.getInfo()

harry.greet()


