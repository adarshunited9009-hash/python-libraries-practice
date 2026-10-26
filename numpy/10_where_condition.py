import numpy as np

ages = np.array([
    [1, 23, 3],
    [4, 25, 6],
    [7, 8, 89]
])

adults = np.where(ages >= 18, ages, "lol")
print("Adults:", adults)
