class Employee:
    language = "python"
    salary = "10000"
    
    def getinfo(self):
        print(f"{self.language}{self.salary}")
    @staticmethod
    def simple():
        print("good night") 
    def __init__(self): #this is dunder method which will be automatically called in python 
        print("enter the application")
mayur = Employee()
mayur.simple()
mayur.getinfo()    