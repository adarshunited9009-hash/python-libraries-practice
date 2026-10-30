import numpy as np

students = np.array([
    "Aman", "Riya", "Rahul", "Priya", "Karan"
])

# Each row represents one student.
# Each column represents one subject.
marks = np.array([
    [78, 85, 69, 90, 88],
    [92, 89, 95, 87, 91],
    [45, 55, 60, 50, 48],
    [30, 40, 35, 55, 45],
    [80, 75, 82, 79, 85]
])

subjects = np.array([
    "Python", "Maths", "Physics",
    "English", "Computer"
])

total = np.sum(marks, axis=1)
print("Total marks:", total)

avg = np.mean(marks, axis=1)
print("Average:", avg)

topper_index = np.argmax(total)
print("Topper is:", students[topper_index])

passed = np.all(marks >= 35, axis=1)
print("Passed students:", students[passed])

failed = np.any(marks < 35, axis=1)
print("Failed students:", students[failed])

subject_avg = np.mean(marks, axis=0)
print("Subject-wise average:", subject_avg)

ranking = np.argsort(total)[::-1]
print("Student ranking:")
for i in ranking:
    print(students[i], total[i])
