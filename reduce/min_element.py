from functools import reduce
nums = [3,77,2,8,9]
result = reduce (lambda x,y:x if x<y else y,nums)
# result = min(nums)
print(result)
