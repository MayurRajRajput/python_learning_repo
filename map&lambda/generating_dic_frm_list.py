# generating a dictionary from two lists

keys=["a","b","c"]
values=[1,2,3]
result=map(lambda k,v:(k,v),keys,values)
print(dict(result))