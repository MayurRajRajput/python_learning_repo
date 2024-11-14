# class Programmer:
#    company = "Microsoft"
#    def __init__(self,name,salary,pincode):
#        self.name=name
#        self.salary = salary
#        self.pincode=pincode
# p = Programmer("mayur",120000,571601)       
# print(p.name,p.salary,p.pincode)
        
# class Calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         print(f"the square is {self.n*self.n}")    
#     def cute(self):
#         print(f"the square is {self.n*self.n*self.n}")    
#     def squareroot(self):
#         print(f"the square is {self.n**1/2}")    
# a = Calculator(4) 
# a.square()
# a.cute()
# a.squareroot()

# class Demo:
#     a=4
# o = Demo()
# print(o.a)    
# o.a=0
# print(o.a)    
# print(Demo().a) 

# class Calculator:
#     def __init__(self,n):
#         self.n = n
#     @staticmethod    
#     def greet():
#         print("hello")    
#     def square(self):
#         print(f"the square is {self.n*self.n}")    
#     def cute(self):
#         print(f"the square is {self.n*self.n*self.n}")    
#     def squareroot(self):
#         print(f"the square is {self.n**1/2}")    
# a = Calculator(4)
# a.greet() 
# a.square()
# a.cute()
# a.squareroot() 

# import random
# class Train:
#     def __init__(self,trainno):
#         self.trainno = trainno
#     def book(self,fro,to):
#         print(f"Ticket is booked in tain no:{self.trainno} form {fro} to {to}")
#     def getstatus(self):
#         print(f"Ticket no:{self.trainno} is running on time")
        
#     def getFare(self,fro,to):
#         print(f"Ticket fare is booked in tain no:{self.trainno} form {fro} to {to} is {random.randint(255,5555)}")
# t = Train(12399)
# t.book("mysuru","bangalore")
# t.getstatus()
# t.getFare("mysuru","bangalore")

import random
class Train:
    def __init__(slf,trainno):
        slf.trainno = trainno
    def book(slf,fro,to):
        print(f"Ticket is booked in tain no:{slf.trainno} form {fro} to {to}")
    def getstatus(slf):
        print(f"Ticket no:{slf.trainno} is running on time")
        
    def getFare(slf,fro,to):
        print(f"Ticket fare is booked in tain no:{slf.trainno} form {fro} to {to} is {random.randint(255,5555)}")
t = Train(12399)
t.book("mysuru","bangalore")
t.getstatus()
t.getFare("mysuru","bangalore")
