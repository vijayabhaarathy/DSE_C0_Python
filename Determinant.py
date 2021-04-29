#4. Write a NumPy program to compute the determinant of a given square array.

import numpy as np
arr1=([1,2,3])
arr2=([3,4,5])
arr3=([6,7,8])

cons_arr=np.array([arr1,arr2,arr3])
arr_det=np.linalg.det(cons_arr)

print(arr_det)
