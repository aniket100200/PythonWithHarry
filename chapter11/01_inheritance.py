class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder:
    language="Python"
    def printLang(self):
        print(f"Out of all the languages here is your language: {self.language}")
# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"The name is {self.name} and and he is good  programmer in {self.language} language")

class Programmer(Employee,coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and and he is good  programmer in {self.language} language")
    

a=Employee()
b=Programmer()
b.name="Aniket"
b.salary=123
b.printLang()

