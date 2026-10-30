import numpy as np

arr = np.array([[1], [3], [np.nan]])

result = np.isnan(arr)
count = np.sum(result)

print("NaN values:", result)
print("Total NaN values:", count)
