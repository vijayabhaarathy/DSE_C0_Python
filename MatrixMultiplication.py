#6. Write a NumPy program to multiple three matrices each of 3*3 dimension.

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,4,5])
arr3=np.array([6,7,8])

arr_mul=np.matmul(arr1,arr2,arr3)

print(arr_mul)
