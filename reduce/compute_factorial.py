from functools import reduce
n=5
result=reduce(lambda x,y:x*y,range(1,n+1))
print(result)