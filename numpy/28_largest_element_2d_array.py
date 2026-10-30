import numpy as np

largest = 0
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

for i in range(3):
    for j in range(3):
        if largest < arr[i][j]:
            largest = arr[i][j]

print("Largest element:", largest)
