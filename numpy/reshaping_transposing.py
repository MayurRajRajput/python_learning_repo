import numpy as np
arr=np.arange(1,13)
print("Original Array: ",arr)
reshaped=arr.reshape(3,4)
print("Reshaped Array(3x4):\n", reshaped)
transposed=reshaped.T
print("Transposed Array:\n", transposed)