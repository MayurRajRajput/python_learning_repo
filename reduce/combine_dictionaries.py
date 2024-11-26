from functools import reduce
dicts=[{"a":2,"b":5},{"a":3,"b":6},{"a":7,"b":1}]
result=reduce(lambda x,y:{key: x.get(key,0)+y.get(key,0) for key in set(x)|set(y)},dicts)
print(result)