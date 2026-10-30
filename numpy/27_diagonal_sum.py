import numpy as np

total = 0
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if i == j:
            print(arr[i][j])
            total = arr[i][j] + total

print("Sum of diagonal elements:", total)
