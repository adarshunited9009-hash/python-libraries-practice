import numpy as np

arr = np.array([1, 89, 67, 45, 23, 12, 34, 56, 78, 90])

result = np.where(arr > 25, "greater than 25", "not greater than 25")
print(result)
