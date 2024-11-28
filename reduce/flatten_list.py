from functools import reduce 
list_of_lists =[[1,2],[3,4],[5,6]]
result = reduce(lambda x,y:x+y,list_of_lists)
print(result)