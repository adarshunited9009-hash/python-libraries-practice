import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

for i in range(3):
    largest = arr[i][0]
    col_index = 0

    for j in range(3):
        if arr[i][j] > largest:
            largest = arr[i][j]
            col_index = j

    print("Row:", i)
    print("Maximum element:", largest)
    print("Column:", col_index)
