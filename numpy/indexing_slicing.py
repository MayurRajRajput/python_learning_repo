import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("element at (0,1)",arr[0,1])
print("First Row",arr[0,:])
print("First Column",arr[:,0])
print("subarray:\n",arr[1:3,1:3])