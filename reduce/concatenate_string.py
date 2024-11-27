from functools import reduce
words = ["python","is","easy"]
result1 = reduce(lambda x,y :x+" "+y,words)
result2 = " ".join(words)
print(result1)
print(result2)
