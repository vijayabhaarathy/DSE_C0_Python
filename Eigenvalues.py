#5. Write a NumPy program to compute the eigenvalues and right eigenvectors of a given square array.

import numpy as np
arr1=([1,2])
arr2=([3,4])

arr_eigval=np.linalg.eigvals([arr1,arr2])
print(np.linalg.eig([arr1,arr2]))
