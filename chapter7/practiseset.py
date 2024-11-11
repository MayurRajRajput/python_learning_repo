# n = int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")


# i=["Harry","Soham","Sathin","Rahul"]
# for name in i:
#     if(name.startswith("S")):
#         print(name)


# n = int(input("enter a number: "))
# i=1
# while(i<=10):
#     print(f"{n}x{i}={n*i}")
#     i=i+1

# n = int(input("enter the number"))
# for i in range(2,n):
#     if(n%i) == 0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")    

# n = int(input("enter the number"))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(f"{sum}")

# n = int(input("enter the number"))
# sum=1
# for i in range(2,n+1):
#     sum=sum*i
# else:
#     print(f"{sum}")

# n=int(input("enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")
    
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print("")

'''
***
* *
***
'''
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print(" ") 
n=int(input("enter the number"))
for i in range(1,11):
       print(f"{n} x {11-i} = {n*(11-i)}")