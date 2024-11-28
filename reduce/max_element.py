from functools import reduce
nums=[5,8,33,9,0]
result=reduce(lambda x,y:x if x>y else y ,nums)
# result=max(nums)
print(result)