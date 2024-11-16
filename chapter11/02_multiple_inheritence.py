# in the multiple inheritance is which here two parent and one child will be inhereted

class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"the name of the Employee is {self.name} and the company is {self.company}")
class Coder:
     language = "Python"
     def printLanguage(self):
         print(f"out of all the language here is your language:{self.language}")   
class programmer(Employee,Coder):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
a = Employee()
b = programmer()

b.show()
b.printLanguage()
b.showLanguage()                     
        