class Employee:
    a= 1
    # def show(self):
    #     print(f"the class attribute of a {self.a}") 
    #when ever we want to print class attribute we will use this method
    @classmethod
    def show(cls):
        print(f"the class attribute of a {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = Employee()
e.a = 45
e.name = "harry khan"
print(e.name)
e.show()        