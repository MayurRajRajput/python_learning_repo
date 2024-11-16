class Employee:
    company = "itc"
    def show(self):
        print(f"the name of the employee is{self.name} and the salary is {self.salary}")
class programmer(Employee):
    company="itc infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language}language")
a = Employee()
b = programmer()
print(a.company,b.company)        