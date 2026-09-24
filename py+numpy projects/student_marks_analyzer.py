# Project 1 → Student Marks Analyzer

# Create a NumPy array of marks
# Calculate average
# Find highest/lowest
# Find students above average
# Sort marks
# Assign grades

import numpy as np

names = ["aishu", "gia", "katie", "max", "troy"]
arr = np.array([[80,60,94,55,50],
                [19,71,82,69,11],
                [70,72,37,74,13],
                [78,58, 78, 34,93],
                [45,60,11,84,75]

])

total = np.sum(arr, axis =0)

avg = np.average(arr, axis = 0)
print(avg)
for name, avg1 in zip(names, avg):
    print("average of", name,"=", avg1)
for tot, name in zip(total, names):
    print("summation", name,"=", tot)

highest = np.max(total)
print("highest marks = ", highest)
lowest = np.min(total)
print("lowest marks = ", lowest)

highest_student = np.argmax(total)
print("highest student is =", names[highest_student])

print(np.sort(arr, axis = None))

grades = np.where(
    arr >= 90, "A",
    np.where(
        arr >= 80, "B",
        np.where(
            arr >= 70, "C",
            np.where(
                arr >=50, "D",
                "fail"
            )
        )
    )
)
print(grades)