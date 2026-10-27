import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

smallest = np.min(arr)
largest = np.max(arr)

smallest_index = np.argmin(arr)
largest_index = np.argmax(arr)

print("Smallest element:", smallest)
print("Index of smallest:", smallest_index)

print("Largest element:", largest)
print("Index of largest:", largest_index)
