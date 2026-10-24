import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Select the first row
print(arr[0, :])

# Select the second column
print(arr[:, 1])

# Select the first two rows and columns
print(arr[0:2, 0:2])
