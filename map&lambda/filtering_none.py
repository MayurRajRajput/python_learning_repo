# filtering None from given list 
data =[None,"python","words",None,"code"]
result=map(lambda x:"missing " if x is None else x,data)
print(list(result))