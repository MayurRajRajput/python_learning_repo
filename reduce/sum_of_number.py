from functools import reduce
num= [10,20,30,40,50]
result=reduce(lambda x,y:x+y,num)
print(result)