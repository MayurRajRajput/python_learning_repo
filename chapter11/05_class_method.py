class Employee:
    a= 1
    # def show(self):
    #     print(f"the class attribute of a {self.a}") 
    #when ever we want to print class attribute we will use this method
    @classmethod
    def show(cls):
        print(f"the class attribute of a {cls.a}")
    
e = Employee()
e.a = 45
e.show()        