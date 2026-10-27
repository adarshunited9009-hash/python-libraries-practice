import numpy as np

arr = np.array([1, 2, 3, 5, 6, 7, -4, -7, -6, -5, -4])
result = np.where(arr < 0, "0", "positive")
print(result)
