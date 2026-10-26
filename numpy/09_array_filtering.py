import numpy as np

age = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16]
])

teenagers = age[age < 18]
adults = age[age >= 18]
senior = age[age >= 60]
even = age[age % 2 == 0]
odd = age[age % 2 != 0]

print("Teenagers:", teenagers)
print("Adults:", adults)
print("Senior:", senior)
print("Even numbers:", even)
print("Odd numbers:", odd)
