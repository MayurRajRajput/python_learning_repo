# using map() with nested data structure
data = [
    {"name":"alice","age":30},
    {"name":"bob","age":20},
    {"name":"Charlie","age":40}
]

result=map(lambda x:x['name'],data )
print(list(result))