class Employee:
    def __init__(self):
        print("consructor of employee")
    a= 1
class Programmer(Employee):
    def __init__(self):
        super().__init__() # it is getting from the parent or superior
        print("consructor of employee")
    b=1
class Manager(Programmer):
    c=1
o = Employee()
print(o.a)

o = Programmer()
print(o.a,o.b)


