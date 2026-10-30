import numpy as np

arr = np.array([1, 3, 78, 45, 90, 67])

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num

print("Second largest element:", second_largest)
