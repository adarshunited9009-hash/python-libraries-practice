import numpy as np

# NumPy Practice Questions
# Try each question yourself before checking any hints.
# Run this file in VS Code and replace each TODO with your solution.

# --------------------------------------------------
# Question 1: Create an array containing numbers 1 to 20.
# --------------------------------------------------
# TODO: Create the array and print it.


# --------------------------------------------------
# Question 2: Create a 3x4 array containing numbers 1 to 12.
# --------------------------------------------------
# TODO: Use np.arange() and reshape().


# --------------------------------------------------
# Question 3: From the array below, select all values greater than 25.
# --------------------------------------------------
numbers = np.array([10, 35, 22, 48, 15, 30, 7])
# TODO: Use Boolean indexing.


# --------------------------------------------------
# Question 4: Find all even numbers in the array.
# --------------------------------------------------
values = np.array([3, 8, 11, 14, 19, 22, 27, 30])
# TODO: Use the modulo operator and Boolean indexing.


# --------------------------------------------------
# Question 5: Replace every value below 18 with 0.
# --------------------------------------------------
ages = np.array([12, 18, 25, 9, 34, 16, 21])
# TODO: Use np.where().


# --------------------------------------------------
# Question 6: Find the sum of each row and each column.
# --------------------------------------------------
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# TODO: Use np.sum() with axis=0 and axis=1.


# --------------------------------------------------
# Question 7: Calculate the mean, median, minimum, and maximum.
# --------------------------------------------------
scores = np.array([72, 85, 91, 66, 78, 95, 81])
# TODO: Use NumPy functions.


# --------------------------------------------------
# Question 8: Add [10, 20, 30] to every row of this matrix.
# --------------------------------------------------
matrix2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
addition = np.array([10, 20, 30])
# TODO: Use broadcasting. Do not use a loop.


# --------------------------------------------------
# Question 9: Find the index of the largest value.
# --------------------------------------------------
marks = np.array([56, 89, 74, 96, 68])
# TODO: Use np.argmax().


# --------------------------------------------------
# Question 10: Normalize the array to a range from 0 to 1.
# Hint: subtract the minimum, then divide by (maximum - minimum).
# --------------------------------------------------
data = np.array([10, 20, 30, 40, 50])
# TODO: Calculate the normalized array.


# --------------------------------------------------
# Bonus: Random simulation
# Generate 100 random integers from 1 to 6 and count each result.
# --------------------------------------------------
# TODO: Use np.random.default_rng(), then np.unique() with return_counts=True.
