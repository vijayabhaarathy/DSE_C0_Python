#7. Explore the Linear Algebra support provided by NumPy.

# 10 cofee + 12 tea = Rs. 52
# 21 cofee + 30 tea = Rs. 103

import numpy as np
arr1 = np.array([[10,12],[21,30]])
arr2 = np.array([52,103])
cost = np.linalg.solve(arr1,arr2)

print(cost)
