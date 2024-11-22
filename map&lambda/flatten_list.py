# flatten a list of tuple
tuples=[(1,2),(3,4),(4,5)]
res=map(lambda x:sum(x),tuples)
print(list(res))
