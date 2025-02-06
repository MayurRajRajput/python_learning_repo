import numpy as np
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Data: ",data)
print("mean: ",np.mean(data))
print("Row-wise Mean:",np.mean(data,axis=1)) 
print("column-wise Mean:",np.mean(data,axis=0))
print("standard Deviation: ",np.std(data,axis=0))
print("variance: ",np.var(data))
 