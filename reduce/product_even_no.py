from functools import reduce
nums=[1,2,3,4,5,6]
result=reduce(lambda x,y:x*y,filter(lambda x:x%2==0,nums ))
print(result)