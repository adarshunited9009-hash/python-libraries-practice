import numpy as np

arr = np.array([100, 11, 89, 2, 3, 2, 1, 4, 5, 6,
                5, 6, 4, 3, 5, 8, 8, 6, 9, 87, 6, 5])

result = np.unique(arr)
print("Unique values in sorted order:", result)
