class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name =name
        self.salary=salary
        self.pincode=pincode
    def toString(self):
        return f"name:'{self.name}',salary:'{self.salary}'"

harry=Programmer("Harry",120000,128523)
print(harry.toString())
aniket=Programmer("Aniket",780000,441924)
print(aniket.toString())
        