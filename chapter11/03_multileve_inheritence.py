# here multilevel inheritance is which have one parent and two child and getting inherited
class Employee:
    a= 1
class Programmer(Employee):
    b=1
class Manager(Programmer):
    c=1
o = Employee()
print(o.a)# print the a attribute
# print(o.b) # show an error as there is no b attribute in employee class

o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)
