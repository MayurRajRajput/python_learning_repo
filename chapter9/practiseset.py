# f=open("poem.txt")
# c = f.read()
# if("twinkle" in c):
#     print("twinkle is present")
# else:
#     print("it is not present")    
# f.close()

# import random
# def game():
   
#     print("you r playing the game...")
#     score = random.randint(1,62)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0    
#     print(f"your score: {score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
# game()

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table +=f"{n} X {i} = {n*i}\n"
#     with open(f"table/table_{n}.txt","w") as f:
#         f.write(table)
# for i in range(2,21):
#     generateTable(i)
# words = ["Donkey","Name","Such"]
# with open("myfile.txt") as f:
#     content = f.read()
# for word in words:   
#     content = content.replace(word,"#"*len(word))
# with open("myfile.txt","w") as f:
#     f.write(content) 

# lineno = 1
# with open("log.txt") as f:
#     lines = f.readlines()
# for line in lines:
#     if("python" in line):
#         print(f"content is present,lineno:{lineno}")
#         break    
#     lineno +=1    
# else:
#     print("content is not present")
# with open("this.txt") as f:
#     content = f.read()
# with open("this_copy.txt","w") as f:
#     f.write(content)      

# with open("file1.txt") as f:
#     content1=f.read()
# with open("file2.txt") as f:
#     content2=f.read()
# if(content1 == content2):
#     print("yes,these files are identical")
# else:        
#     print("no,these files are not identical")    

# with open("this_copy.txt","w") as f:
#     f.write("")
import os
with open("log.txt") as f:
    content = f.read()
with open("renamed_log.txt","w") as f:
    f.write(content)
    os.remove("log.txt")    
                       