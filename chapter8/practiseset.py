# a=int(input("enter the number1: "))
# b=int(input("enter the number2: "))
# c=int(input("enter the number3: "))
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return print(f"{a} is greatest")
#     elif(b>a and b>c):
#         return print(f"{b} is greatest")
#     else:
#         return print(f"{c} is greatest ")       
# greatest(a,b,c)    


# c/5 = (f-32)/9
# cel=int(input("enter the cel: "))
# def f_to_c(cel):
#     fara=((9/5)*cel)+32
#     return fara
# print(f"{f_to_c(cel)}°F") 
   
# f=float(input("enter the faranheit: "))
# def f_to_c(f):
#     c=((f-32)*5)/9
#     return c
# print(f"{f_to_c(f)}° C")    
# print(f"{round(f_to_c(f),2)}° C")    

# def sum(n):
#     if(n==1):
#         return 1
#     return n+sum(n-1)
# print(sum(5))

# def dot(n):
#     if(n==0):
#         return
#     print("*"*n)
#     dot(n-1)
# dot(5)    

# def inch_2_cent(n):
#     cm = n*2.54
#     return cm
# n = int(input("enter the inches: "))
# print(f" {n} inches = {round(inch_2_cent(n),2)} cm")  
  
# l=["Harry","Praveen","shuban","an"]
# def list_remove(l,word):
#     n=[]
#     for i in l:
#         if not(i==word):
#             n.append(i.strip(word))
#     return n
# print(list_remove(l,"an"))    

def mul(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
mul(5)       