class Employee:
    language = "python"
    salary = "10000"
    
    def getinfo(self):
        print(f"{self.language}{self.salary}")
    @staticmethod
    def simple():
        print("good night")    
mayur = Employee()
mayur.simple()
mayur.getinfo()    