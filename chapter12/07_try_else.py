try:
    a= int(input("hey,Enter a number :"))
    print(a)
except Exception as e:
    print(e)
else:
    print("iam inside else")    #when try is successfull then it will come to else
