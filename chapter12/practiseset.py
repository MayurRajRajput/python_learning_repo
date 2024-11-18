# try:
#     with open("1.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("3.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# print("thank you")

# l=[1,2,3,4,5,6,7,8]
# for i,item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)


# n=int(input("enter the number"))

# multipliction=[n*i for i in range(1,11) ]
# print(multipliction)

# try:
#     a=int(input("enter a: "))
#     b=int(input("enter b: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("infinite")

n=int(input("enter the number"))

multipliction=[n*i for i in range(1,11) ]
print(multipliction)
with open("Tables.txt","w") as f:
    f.write(str(multipliction)+"\n")
