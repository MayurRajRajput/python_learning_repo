# for finding fahrenheit we want to use this formula
# fahrenheit=(c*9/5)+32

celsius= [0,20,37,100]
fahrenheit=map(lambda c:(c*9/5)+32,celsius)
print(list(fahrenheit))