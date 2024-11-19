# name = input("enter the name")
# marks = int(input("enter the marks"))
# phone= int(input("enter the number"))
# a = "The name of the student is {},his marks are {} and phone number is {}".format(name,marks,phone)
# print(a)

# table= [str(7*i) for i in range(1,11)]
# s="\n".join(table)
# print(s)

# def divible5(n):
#     if(n%5==0):
#         return True
#     return False
# a=[1,4,10,536,5643,55,4563,32455,7676,3344]
# print(list(filter(divible5,a)))

# from functools import reduce
# a=[1,4,10,536,5643,55,4563,32455,7676,3344]

# def greater(a,b):
#     if(a>b):
#         return a
#     return b
# s=reduce(greater,a)
# print(s)

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return"<p>Hello world!</p>"
