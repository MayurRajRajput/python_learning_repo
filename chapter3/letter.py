name= input("enter the name")
date=input("enter the date")
letter='''
dear <|Name|>,
you are selected!
<|Date|>
'''
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))